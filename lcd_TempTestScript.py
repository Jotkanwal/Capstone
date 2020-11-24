from w1thermsensor import W1ThermSensor #https://pypi.org/project/w1thermsensor/
from lcd_16x2 import lcd_16x2 #see lcd16_2.py
from datetime import datetime #used for creating timestamps
import time #used for waiting
import RPi.GPIO as GPIO #raspi pin control

HEATER_RELAY_PIN = 21
LCD = lcd_16x2();
DS18B20_SENSOR = W1ThermSensor();

flag = True;
times_above_desired = 1;
relay = False;
desired_temp = 20;
LCD.lcd_init();
GPIO.setmode(GPIO.BCM);
GPIO.setup(HEATER_RELAY_PIN, GPIO.OUT);

def relay_on():
    GPIO.output(HEATER_RELAY_PIN,GPIO.HIGH)

def relay_off():
    GPIO.output(HEATER_RELAY_PIN,GPIO.LOW)

while flag:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S");
    temp = DS18B20_SENSOR.get_temperature();
    
    lcd_lmsg1 = "Cu:%.1f De:%.1f" % (temp, desired_temp);
    lcd_lmsg2 = "Heat:" + str(relay);
            
    print("------------", now, "------------");
    print(lcd_lmsg1);
    print(lcd_lmsg2);
    
    LCD.lcd_string(lcd_lmsg1, LCD.LCD_LINE_1);
    LCD.lcd_string(lcd_lmsg2, LCD.LCD_LINE_2);
    
    if temp < desired_temp:
        print("below");
        if not relay:    
            print("flipped relay on");
            GPIO.output(HEATER_RELAY_PIN,GPIO.HIGH)
            
        relay = True;
    elif temp >= desired_temp:
        print("above");
        if relay:  
            print("flipped relay off");
            GPIO.output(HEATER_RELAY_PIN,GPIO.LOW)
        relay = False;
        times_above_desired += 1;
        flag = times_above_desired <= 2;
    
    time.sleep(2);

print("tempurature reached, shutting down");
LCD.cleanup();
GPIO.cleanup();