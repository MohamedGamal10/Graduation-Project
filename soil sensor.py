import spidev
import time
import os
import RPi.GPIO as gpio

# Start SPI connection
spi = spidev.SpiDev()
spi.open(0,0)

# Read MCP3008 data
def analogInput(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

while True:
  print("Soil Moisture 1: "+str(analogInput(0)))