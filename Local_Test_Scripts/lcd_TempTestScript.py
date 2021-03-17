from w1thermsensor import W1ThermSensor #https://pypi.org/project/w1thermsensor/
from lcd_16x2 import lcd_16x2 #see lcd16_2.py
from datetime import datetime #used for creating timestamps
import time #used for waiting
import RPi.GPIO as GPIO #raspi pin control
import csv
from time import sleep

HEATER_RELAY_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(HEATER_RELAY_PIN, GPIO.OUT)
LCD = lcd_16x2()
DS18B20_SENSOR = W1ThermSensor()
fields = ['Time', 'Temp', 'State']
rows = ['time', 'temp', 'state']
filename = "histogram.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

flag = True
relay = False
desired_temp = 22
duration = 1800 #heater duration in seconds
LCD.lcd_init()
start = time.time();

#digital encoder setup
#clk = 1
#dt = 0
#GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#clkLastState = GPIO.input(clk)


def relay_on(pin):
    print("the heater is switched")
    GPIO.output(pin,GPIO.LOW)

def relay_off(pin):
    GPIO.output(pin,GPIO.HIGH)

def check_encoder():
    global clkLastState
    global desired_temp
    clkState = GPIO.input(clk)
    dtState = GPIO.input(dt)
    if clkState != clkLastState:
            if dtState != clkState:
                    desired_temp += 1
            else:
                    desired_temp -= 1
            print("I changed!!!")
    clkLastState = clkState
    

while flag:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_left = int(time.time() - start)
    flag = (time_left <= duration)
    print(time_left)
    #check_encoder()
    
    try:
        temp = DS18B20_SENSOR.get_temperature()
    except:
        print("temp error, resetting sensor and temp")
        DS18B20_SENSOR = W1ThermSensor()
        temp = desired_temp + 1
    
    if time_left % 5 == 0:
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            rows = [now, str(temp), str(relay)]
            print(rows)
            
            csvwriter.writerow(rows)
        
    lcd_lmsg1 = "Cu:%.1f De:%.1f" % (temp, desired_temp)
    lcd_lmsg2 = "Heat:" + str(relay)
    
    print("------------", now, "------------")
    print(lcd_lmsg1)
    print(lcd_lmsg2)
    
    LCD.lcd_string(lcd_lmsg1, LCD.LCD_LINE_1)
    LCD.lcd_string(lcd_lmsg2, LCD.LCD_LINE_2)
    
    if temp < desired_temp:
        print("below")
        if not relay:
            print("flipped relay on")
            relay_on(HEATER_RELAY_PIN)
        relay = True
    elif temp >= desired_temp:
        print("above")
        if relay:  
            print("flipped relay off")
            relay_off(HEATER_RELAY_PIN)
        relay = False
    
    #time.sleep(0.5)

print("tempurature reached, shutting down")
LCD.cleanup()
GPIO.cleanup()