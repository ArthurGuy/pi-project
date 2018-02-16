#!/usr/bin/python

import Adafruit_DHT
import RPi.GPIO as GPIO
import time

sensor_pin = 26
fan_pin = 4

max_temp = 25

sensor = Adafruit_DHT.DHT22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_pin, GPIO.OUT)

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)

        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading.')

        if temperature is not None:
            if temperature > max_temp:
                GPIO.output(fan_pin, True)
            elif temperature < (max_temp - 1):
                GPIO.output(fan_pin, False) 

        time.sleep(15)
        
except KeyboardInterrupt:
    GPIO.output(fan_pin, False) 
    print('Exiting')
