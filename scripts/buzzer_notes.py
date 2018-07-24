# this script plays one of four random notes on the Passive Buzzer
import RPi.GPIO as GPIO
import time
import random

# breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin number for Passive Buzzer; pin 32 = GPIO 12
buzz_pin = 32

#set Passive Buzzer pin's mode as output
GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)

frequencies = [220, 440, 880, 1760]
n = random.randint(0,3)
Buzz.ChangeFrequency(frequencies[n])
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
