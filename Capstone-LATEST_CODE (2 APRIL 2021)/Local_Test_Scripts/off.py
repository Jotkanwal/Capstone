from lcd_16x2 import lcd_16x2 #see lcd16_2.py
import RPi.GPIO as GPIO #raspi pin control


GPIO.setmode(GPIO.BCM)
LCD = lcd_16x2()


print("resetting LCD..")
LCD.cleanup()
print("resetting GPIO..")
GPIO.cleanup()

print("done")