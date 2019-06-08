#!/usr/bin/python
import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 17)
    #print (humidity)
    print 'Temp: {0:1.1f} C  Humidity: {1:01.1f} %'.format(temperature, humidity)
