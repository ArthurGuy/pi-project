import time
import picamera
import RPi.GPIO as GPIO
import aiy.voicehat
from guizero import App, Text, Picture

from PIL import ImageTk, Image

# export DISPLAY=:0.0

#Ignore warnings about redefining the GPIO port
GPIO.setwarnings(False)

led = aiy.voicehat.get_led()
button = aiy.voicehat.get_button()

preview_mode = 0


def button_take_photo():
    if preview_mode == 1
        led.set_state(aiy.voicehat.LED.BLINK_3)
        time.sleep(2)
        camera.capture('test.jpg')
        led.set_state(aiy.voicehat.LED.PULSE_SLOW)
        camera.stop_preview()
        preview_mode = 0
    else 
        camera.start_preview()
        preview_mode = 1


app = App(title="Camera")

img = ImageTk.PhotoImage(Image.open('test.jpg'))
preview = Text(app, text="Preview")
preview.tk.config(image = img)

camera = picamera.PiCamera()
try:
    
    led.set_state(aiy.voicehat.LED.PULSE_SLOW)
    
    welcome_message = Text(app, text="Photo booth")
    #photo = Picture(app, image="test.jpg")
    
    
    button.on_press(button_take_photo)
    
    
    #button.wait_for_press()
    #led.set_state(aiy.voicehat.LED.BLINK_3)
    #time.sleep(2)
    #camera.capture('test.jpg')
    
    #camera.stop_preview()
    
    app.display()
    
finally:
    camera.close()
