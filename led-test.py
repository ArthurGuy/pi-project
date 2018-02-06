#!/usr/bin/python

import RPi.GPIO as GPIO
import aiy.voicehat

led = aiy.voicehat.get_led()
button = aiy.voicehat.get_button()

led.set_state(aiy.voicehat.LED.PULSE_QUICK)

button.wait_for_press()
