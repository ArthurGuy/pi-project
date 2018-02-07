#!/usr/bin/python

import Adafruit_DHT
import RPi.GPIO as GPIO

sensor = Adafruit_DHT.DHT22
pin = 26

fan_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_pin, GPIO.OUT)

GPIO.output(fan_pin, True)

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')

GPIO.output(fan_pin, False) 
