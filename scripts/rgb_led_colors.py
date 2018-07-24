import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
#this script blinhks one of four random colors on the RGB LED
# colors are R = red, G = green, B = blue, Y = yellow
colors = ['R', 'G', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

n = random.randint(0,3)
LED.setColor(colors[n])
time.sleep(0.5)
LED.noColor()
time.sleep(0.5)
LED.destroy()
