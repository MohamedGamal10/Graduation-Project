import pyrebase
import RPi.GPIO as GPIO
from time import sleep

config = {
  "apiKey": "AIzaSyC5XKJZtmU0uP__u7pj55NKUw_C4ESoa20",
  "authDomain": "rpi-pin.firebaseapp.com",
  "databaseURL": "https://rpi-pin.firebaseio.com",
  "storageBucket": "rpi-pin.appspot.com",
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)



print ("**********    INICIO  *************")

while True:
    salidavalve1 = db.child("valve1").get()
    GPIO.output(27, salidavalve1.val())
    
    salidavalve2 = db.child("valve2").get()
    GPIO.output(5, salidavalve2.val())

    salidavalve3 = db.child("valve3").get()
    GPIO.output(6, salidavalve3.val())

    salidavalve4 = db.child("valve4").get()
    GPIO.output(13, salidavalve4.val())

    salidafan1 = db.child("fan1").get()
    GPIO.output(21, salidafan1.val())

    salidafan2 = db.child("fan2").get()
    GPIO.output(16, salidafan2.val())

    salidaheater = db.child("heater").get()
    GPIO.output(19, salidaheater.val())
    
    
    sleep(1)

GPIO.cleanup()
