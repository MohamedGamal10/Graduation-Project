import pyrebase

config = {
  "apiKey": "AIzaSyC5XKJZtmU0uP__u7pj55NKUw_C4ESoa20",
  "authDomain": "rpi-pin.firebaseapp.com",
  "databaseURL": "https://rpi-pin.firebaseio.com",
  "storageBucket": "rpi-pin.appspot.com",
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()


temperature = 65
humidity = 100

data = {"temperature":temperature}
db.child("temperature").push(data)

