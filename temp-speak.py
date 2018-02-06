import RPi.GPIO as GPIO
import aiy.voicehat

#Ignore warnings about redefining the GPIO port
GPIO.setwarnings(False)

led = aiy.voicehat.get_led()
button = aiy.voicehat.get_button()
audio = aiy.audio

import Adafruit_DHT
sensor = Adafruit_DHT.DHT22
pin = 26

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
  audio.say('The temperature is {0:0.1f} degrees and the humidity is {1:0f}%'.format(temperature, humidity), lang="en-GB", volume=75, pitch=135)
