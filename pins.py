import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(27, gpio.OUT)
gpio.setup(5, gpio.OUT)
gpio.setup(6, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(21, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(12, gpio.OUT)

while 1 :
     gpio.output(21,0)
     gpio.output(16,0)
     gpio.output(12,0)
     gpio.output(27,0)
     gpio.output(5,0)
     gpio.output(6,0)
     gpio.output(13,0)