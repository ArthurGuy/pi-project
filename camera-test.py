import time
import picamera
import RPi.GPIO as GPIO
import aiy.voicehat
from guizero import App, Text, Picture

#Ignore warnings about redefining the GPIO port
GPIO.setwarnings(False)

led = aiy.voicehat.get_led()
button = aiy.voicehat.get_button()

app = App(title="Camera")

welcome_message = Text(app, text="Photo booth")
app.display()

camera = picamera.PiCamera()
try:
    camera.start_preview()
    led.set_state(aiy.voicehat.LED.PULSE_SLOW)
    button.wait_for_press()
    led.set_state(aiy.voicehat.LED.BLINK_3)
    time.sleep(2)
    camera.capture('test.jpg')
    camera.stop_preview()
    
    my_cat = Picture(app, image="test.jpg")
    
finally:
    camera.close()
