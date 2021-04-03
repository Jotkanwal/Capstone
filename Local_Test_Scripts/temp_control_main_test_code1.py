from w1thermsensor import W1ThermSensor #https://pypi.org/project/w1thermsensor/
from lcd_16x2 import lcd_16x2 #see lcd16_2.py
from datetime import datetime #used for creating timestamps
import time #used for waiting
import RPi.GPIO as GPIO #raspi pin control
import mysql.connector #import python-db connector
import Adafruit_DHT #used for DHT humidity sensor

TEMP_DB = mysql.connector.connect(
    host = "localhost",
    user = "test",
    password = "asdf123",
    database = "capstone"
)
sql_cursor = TEMP_DB.cursor(buffered = True);

HEATER_RELAY_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(HEATER_RELAY_PIN, GPIO.OUT)
LCD = lcd_16x2()
DS18B20_SENSOR = W1ThermSensor()
is_time_remaining = True
heater_relay_status = False 
desired_temp = 25 #desired temperature in Celcius
duration = 1800 #timer duration in seconds

LCD.lcd_init()

#digital encoder setup
clk = 1
dt = 0
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

clkLastState = GPIO.input(clk)

#push button setup
up_button = 17
down_button = 27

GPIO.setup(up_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(down_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#DHT humidity sensor setup
global_humidity = 10
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN=23

def set_relay(pin, low_high):
    GPIO.output(pin,low_high);

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
    time.sleep(0.1)

def check_buttons():
    global desired_temp
    if(not GPIO.input(up_button)):
        print("I go up")
        desired_temp += 1
    if(not GPIO.input(down_button)):
        print("I go down")
        desired_temp -= 1
    time.sleep(0.1)

def readHumidity():
    global global_humidity
    humidity, temp = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temp is not None:
        global_humidity = humidity
        print(humidity)

start = time.time();
while is_time_remaining:
    #check time remaining on the timer
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_left = int(time.time() - start)
    is_time_remaining = (time_left <= duration)
    print(duration - time_left)
    check_encoder()
    check_buttons()
    #get temperature from the sensor, reset the temp if it throws a read error
    try:
        temp = DS18B20_SENSOR.get_temperature()
    except:
        print("temp sensor read error, resetting sensors and temperature reading")
        temp = desired_temp + 1
    
    #get humidity
    readHumidity()
    
    #in lieu of db entries, every 5 seconds write a data entry to historgram csv
    if time_left % 5 == 0:
        #uploading to our database
        db_insert = "INSERT INTO data (temperature) VALUES (%s)" % (int(temp));
        print(db_insert);
        sql_cursor.execute(db_insert);
        TEMP_DB.commit();

    #prepare the messages to send to the LCD
    lcd_lmsg1 = "Cu:%.1f De:%.1f" % (temp, desired_temp)
    lcd_lmsg2 = "Heat:" + str(heater_relay_status)
    lcd_lmsg3 = "Humidity:" + str(global_humidity) + "%"
    
    #write LCD messages to terminal for debugging
    print("------------", now, "------------")
    print(lcd_lmsg1)
    print(lcd_lmsg3)
    
    #update LCD
    LCD.lcd_string(lcd_lmsg1, LCD.LCD_LINE_1)
    LCD.lcd_string(lcd_lmsg3, LCD.LCD_LINE_2)
    
    #relay control based on being either above or below the desired temp
    if temp < desired_temp:
        print("below")
        if not heater_relay_status:
            print("flipped relay on")
            set_relay(HEATER_RELAY_PIN, False)
        heater_relay_status = True
    elif temp >= desired_temp:
        print("above")
        if heater_relay_status:  
            print("flipped relay off")
            set_relay(HEATER_RELAY_PIN, True)
        heater_relay_status = False

print("time reached, shutting down")
#cleanup GPIO pin assignments
set_relay(HEATER_RELAY_PIN, True)
LCD.cleanup()
GPIO.cleanup()
