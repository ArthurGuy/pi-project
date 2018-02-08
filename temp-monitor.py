#!/usr/bin/python

import Adafruit_DHT
import RPi.GPIO as GPIO
import time

sensor = Adafruit_DHT.DHT22
pin = 26
max_temp = 20

fan_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_pin, GPIO.OUT)

while True:

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')

    if temperature > max_temp:
        GPIO.output(fan_pin, True)
    elif temperature < (max_temp - 1):
        GPIO.output(fan_pin, False) 

    time.sleep(15)
