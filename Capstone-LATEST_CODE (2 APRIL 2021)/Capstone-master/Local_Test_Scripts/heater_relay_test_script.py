import RPi.GPIO as GPIO
import time

HEATER_RELAY_PIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(HEATER_RELAY_PIN, GPIO.OUT)

def relay_on(pin):
    GPIO.output(pin,GPIO.HIGH)

def relay_off(pin):
    GPIO.output(pin,GPIO.LOW)


try:
    relay_on(HEATER_RELAY_PIN)
    time.sleep(5)
    relay_off(HEATER_RELAY_PIN)
    time.sleep(5)
    GPIO.cleanup()
except KeyboardInterrupt:
    GPIO.cleanup()