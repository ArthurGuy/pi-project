#!/usr/bin/python

import aiy.voicehat

led = aiy.voicehat.get_led()

led.set_state(aiy.voicehat.LED.BLINK)
