#!/usr/bin/python

import aiy._drivers._led

# GPIO definitions (BCM)
_GPIO_BUTTON = 23
_GPIO_LED = 25

# Import LED class to expose the LED constants.
LED = aiy._drivers._led.LED

_voicehat_led = aiy._drivers._led.LED(channel=_GPIO_LED)
_voicehat_led.start()

led.set_state(aiy.voicehat.LED.BLINK)
