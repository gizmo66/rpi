from machine import Pin, ADC
from network import WLAN, STA_IF
import secrets
import ubinascii
import urequests as requests
import time
import ntptime
from math import floor

moisture_sensor = ADC(Pin(26))
temperature_sensor = ADC(4)
led = Pin("LED", Pin.OUT)
led.on()

print("::PICO::")

def round_half_up(n, decimals=0):
    multiplier = 10**decimals
    return floor(n * multiplier + 0.5) / multiplier

def connect():
    global wlan
    wlan = WLAN(STA_IF)
    wlan.active(True)
    wlan.connect(secrets.SSID, secrets.PASSWORD)

    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        if max_wait == 9:
            print('\nwaiting for connection...')
        else:
            print('waiting for connection...')
        time.sleep(1)

    if wlan.status() != 3:
        print('\nError')
    else:
        print('\nConnected to Wi-fi')
        status = wlan.ifconfig()
        print('IP: ' + status[0])
        ip = status[0]

    mac = ubinascii.hexlify(WLAN().config('mac'),':').decode()
    print("\nMAC: " + mac)
    print("channel: " + str(wlan.config('channel')))
    print("essid: " + wlan.config('essid'))
    print("txpower: " + str(wlan.config('txpower')) + "\n")
    return ip

try:
    ip = connect()
except OSError as e:
    print(e)
    print('\nRestarting microcontroller...')
    time.sleep(3)
    machine.reset()

ntptime.settime()

count = 0
rSum = 0.0
mSum = 0.0
tSum = 0.0

while True:

    moisture_raw = 65535 - moisture_sensor.read_u16()
    moisture = (moisture_raw + 1.0) / 600.0

    reading = temperature_sensor.read_u16() * (3.3 / (65535))
    temperature = 27 - (reading - 0.706)/0.001721

    rSum = rSum + moisture_raw
    mSum = mSum + moisture
    tSum = tSum + temperature

    if count == 60:

        y, m, d, h, mm, s, wd, yd = time.localtime()

        dt_format = "{:02d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}"
        dt = dt_format.format(y, m, d, h+1, mm, s) + ","
        rm_value = (int)(round_half_up(rSum / 60.0))
        rm = str(rm_value) + ","
        rt = str(tSum / 60.0) + ","
        m = str((int)(round_half_up(mSum / 60.0))) + ","
        t = str((int)(round_half_up(tSum / 60.0))) + ","

        levels = ["wet", "moist", "dry", "very dry"]

        s = ""
        if rm_value >= 42000:
            s = levels[0]
        if rm_value < 42000 and rm_value >= 38000:
            s = levels[1]
        if rm_value < 38000 and rm_value >= 34000:
            s = levels[2]
        if rm_value < 34000:
            s = levels[3]

        data = dt + rm + rt + m + t + s

        print(data)

        try:
            led.on()
            body = {"path": "/home/pi/Desktop/repo/rpi/baobab.csv","row": data}
            r = requests.post("http://rpi-zero-w-v1:8080/add-reading", json=body)
            r.close()
        except OSError as e:
            print(e)
            led.off()

        mSum = 0.0
        rSum = 0.0
        tSum = 0.0
        count = 0

    time.sleep(1)
    count = count + 1
