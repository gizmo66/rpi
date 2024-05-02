from time import sleep
import os

while True:
    os.system("cd /home/pi/Desktop/repo/rpi/ && gnuplot -e \"datafile='baobab.csv'; load 'settings_baobab.gp'\" plot.gp")
    sleep(60)
    os.system("cd /home/pi/Desktop/repo/rpi/ && git add . && git commit -m \"update\" && git push")
    sleep(240)
