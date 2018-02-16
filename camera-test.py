import time
import picamera
import RPi.GPIO as GPIO
import aiy.voicehat

# export DISPLAY=:0.0

#Ignore warnings about redefining the GPIO port
GPIO.setwarnings(False)

led = aiy.voicehat.get_led()
button = aiy.voicehat.get_button()



try:
    camera = picamera.PiCamera()
    camera.rotation = 0
    camera.preview_fullscreen = False

    camera.resolution = (640, 360)
    camera.start_preview()
    camera.preview.window = (192, 100, 640, 360)
    
finally:
    camera.close()
