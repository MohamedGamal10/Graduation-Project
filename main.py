#!/usr/bin/python
import sys
import Adafruit_DHT
import spidev
import time
import os
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(27, gpio.OUT)
gpio.setup(5, gpio.OUT)
gpio.setup(6, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(21, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(12, gpio.OUT)

# Start SPI connection
spi = spidev.SpiDev()
spi.open(0,0)

# Read MCP3008 data
def analogInput(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

while True:
    
    humidity, temperature = Adafruit_DHT.read_retry(11, 17)
    print 'Temp: {0:1.1f} C  Humidity: {1:01.1f} %'.format(temperature, humidity)
    print("        ")
    print("Soil Moisture 1: "+str(analogInput(0)))
    print("Soil Moisture 2: "+str(analogInput(1)))
    print("Soil Moisture 3: "+str(analogInput(2)))
    print("Soil Moisture 4: "+str(analogInput(3)))
    print("        ")
    
    if temperature>19:
	gpio.output(21,1)
	gpio.output(16,1)
        print("Fan 1 on,Fan 2 on")
    elif temperature<19:
	gpio.output(21,0)
	gpio.output(16,0)
        gpio.output(12,1)
        print("Fan 1 off,Fan 2 off ,Heater on" )

    if analogInput(0)>500:
	gpio.output(27,1)
        print("Valve 1 on")
    elif analogInput(0)<500:
	gpio.output(27,0)
        print("Valve 1 off")

    if analogInput(1)>500:
	gpio.output(5,1)
        print("Valve 2 on")
    elif analogInput(1)<500:
	gpio.output(5,0)
        print("Valve 2 off")

    if analogInput(2)>500:
	gpio.output(6,1)
        print("Valve 3 on")
    elif analogInput(2)<500:
	gpio.output(6,0)
        print("Valve 3 off")

    if analogInput(3)>500:
	gpio.output(13,1)
        print("Valve 4 on")
    elif analogInput(3)<500:
	gpio.output(13,0)
        print("Valve 4 off")

    print("        ")