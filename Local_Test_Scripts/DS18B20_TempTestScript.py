from w1thermsensor import W1ThermSensor #https://pypi.org/project/w1thermsensor/
from datetime import datetime #used for creating timestamps
import time #used for waiting
import mysql.connector #import python-db connector

DS18B20_SENSOR = W1ThermSensor()
'''
TEMP_DB = mysql.connector.connect(
    host = "localhost",
    user = "test",
    password = "asdf123",
    database = "capstone"
)

sql_cursor = TEMP_DB.cursor(buffered = True);
'''
while True:   
    #defining current time and getting the temps from the DS18B20
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S");
    temps = DS18B20_SENSOR.get_temperatures([
        W1ThermSensor.DEGREES_C,
        W1ThermSensor.DEGREES_F,
        W1ThermSensor.KELVIN]);
    
    #uploading to our database
    #db_insert = "INSERT INTO data (temp) VALUES (%s)" % (int(temps[0]));
    #sql_cursor.execute(db_insert);
    #TEMP_DB.commit();
    
    #printing a formatted terminal entry
    print("------------", now, "------------");
    print("The temperature is %s C, %s F, %s K" % (temps[0], temps[1], temps[2]));
    #print(db_insert);
    
    #wait two seconds
    time.sleep(2);
