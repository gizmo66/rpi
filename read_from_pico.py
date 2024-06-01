from time import sleep
import os

while True:
    os.system("cd /home/pi/Desktop/repo/rpi/ && gnuplot -e \"datafile='baobab.csv'; load 'settings_baobab.gp'\" plot.gp")
    sleep(15)
    os.system("cd /home/pi/Desktop/repo/rpi/ && git add .")
    sleep(15)
    os.system("cd /home/pi/Desktop/repo/rpi/ && git commit -m \"update\"")
    sleep(15)
    os.system("cd /home/pi/Desktop/repo/rpi/ && git push")
    sleep(15)
