import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

up_button = 17
down_button = 27

GPIO.setup(up_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(down_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if(not GPIO.input(up_button)):
        print("I go up")
    if(not GPIO.input(down_button)):
        print("I go down")
    time.sleep(0.1)