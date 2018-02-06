import time
import picamera
import RPi.GPIO as GPIO
import aiy.voicehat

#Ignore warnings about redefining the GPIO port
GPIO.setwarnings(False)

led = aiy.voicehat.get_led()
button = aiy.voicehat.get_button()

camera = picamera.PiCamera()
try:
    camera.start_preview()
    led.set_state(aiy.voicehat.LED.PULSE_SLOW)
    button.wait_for_press()
    led.set_state(aiy.voicehat.LED.BLINK_3)
    time.sleep(2)
    camera.capture('test.jpg')
    camera.stop_preview()
finally:
    camera.close()
