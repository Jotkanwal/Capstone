from w1thermsensor import W1ThermSensor #https://pypi.org/project/w1thermsensor/
from datetime import datetime #used for creating timestamps
import time #used for waiting

DS18B20_SENSOR = W1ThermSensor()

while True:   
    #defining current time and getting the temps from the DS18B20
    now = datetime.now().strftime("%H:%M:%S")
    temps = DS18B20_SENSOR.get_temperatures([
    	W1ThermSensor.DEGREES_C,
    	W1ThermSensor.DEGREES_F,
    	W1ThermSensor.KELVIN]);
	
    #printing a formatted ssh entry
    print("------------", now, "------------");
    print("The temperature is %s C, %s F, %s K"
          % (temps[0], temps[1], temps[2]));
	
    #wait two seconds
    time.sleep(2);
