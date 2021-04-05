#if python doesn't recognize this do sudo pip3 install Adafruit_DHT
import Adafruit_DHT
import time

#variable assignments for the data pin and sensor data stream
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN=23

#the loop waits 3 seconds every pass, then reads the data streamed
#from the gpio pins to the pi and displays temperature in Celcius
#and the humidity as a percentage. It then writes it into the terminal
while True:
    humidity, temp = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temp is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temp,humidity))
        print(humidity)
    else:
        print("Sensor failure");
    time.sleep(3);