from w1thermsensor import W1ThermSensor #https://pypi.org/project/w1thermsensor/
import dht11 #https://pypi.org/project/dht11/
from lcd_16x2 import lcd_16x2 #see lcd16_2.py
from datetime import datetime #used for creating timestamps
import time #used for waiting
import RPi.GPIO as GPIO #raspi pin control
import mysql.connector #import python-db connector

def set_relay(pin, low_high):
    GPIO.output(pin,low_high);

def temp_control(desired_temp, duration):
    TEMP_DB = mysql.connector.connect(
        host = "localhost",
        user = "test",
        password = "asdf123",
        database = "capstone"
    )
    sql_cursor = TEMP_DB.cursor(buffered = True);
    #variables
    HEATER_RELAY_PIN = 21
    HEATER_LED_PIN = 24
    temp = 0
    cur_humidity = 0
    is_time_remaining = True
    heater_relay_status = False
    #GPIO Prep and assignments
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(HEATER_RELAY_PIN, GPIO.OUT)
    GPIO.setup(HEATER_LED_PIN, GPIO.OUT)
    #LCD and sensor setup
    LCD = lcd_16x2()
    DS18B20_SENSOR = W1ThermSensor()
    DHT11_SENSOR = dht11.DHT11(pin = 23)
    LCD.lcd_init()

    start = time.time();
    while is_time_remaining:
        #check time remaining on the timer
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_left = int(time.time() - start)
        is_time_remaining = (time_left <= duration)
        print(duration - time_left)

        #get temperature from the sensor, reset the temp if it throws a read error
        try:
            temp = DS18B20_SENSOR.get_temperature()
        except:
            print("temp sensor read error, resetting temperature reading")
            temp = desired_temp + 1

        #get humidity
        readout = DHT11_SENSOR.read()
        if readout.is_valid():
            cur_humidity = readout.humidity

        #upload to our database every 5 seconds
        if time_left % 5 == 0:
            db_insert = "INSERT INTO data (temperature, humidity) VALUES (%s, %s)",  (int(temp), int(cur_humidity));
            print(db_insert);
            sql_cursor.execute(db_insert);
            TEMP_DB.commit();

        #prepare the messages to send to the LCD
        lcd_lmsg1 = "Cu:%.1f De:%.1f" % (temp, desired_temp)
        lcd_lmsg2 = "Humidity:" + str(cur_humidity) + "%"

        #write LCD messages to terminal for debugging
        print("------------", now, "------------")
        print(lcd_lmsg1)
        print(lcd_lmsg2)

        #update LCD
        LCD.lcd_string(lcd_lmsg1, LCD.LCD_LINE_1)
        LCD.lcd_string(lcd_lmsg2, LCD.LCD_LINE_2)

        #relay control based on being either above or below the desired temp
        if temp < desired_temp:
            print("below")
            if not heater_relay_status:
                print("flipped relay on")
                set_relay(HEATER_RELAY_PIN, False)
                GPIO.output(HEATER_LED_PIN, True)
            heater_relay_status = True
        elif temp >= desired_temp:
            print("above")
            if heater_relay_status:
                print("flipped relay off")
                set_relay(HEATER_RELAY_PIN, True)
                GPIO.output(HEATER_LED_PIN, False)
            heater_relay_status = False

    print("time reached, shutting down")
    #cleanup GPIO pin assignments
    set_relay(HEATER_RELAY_PIN, True)
    LCD.cleanup()
    GPIO.cleanup()
