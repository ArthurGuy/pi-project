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


def button_take_photo():
    led.set_state(aiy.voicehat.LED.BLINK_3)
    time.sleep(2)
    camera.capture('test.jpg')
    led.set_state(aiy.voicehat.LED.PULSE_SLOW)


app = App(title="Camera")

img = ImageTk.PhotoImage(Image.open('test.jpg'))
preview = Text(app, text="Preview")
panel = preview.tk.Label(none, image = img)

camera = picamera.PiCamera()
try:
    camera.start_preview()
    #led.set_state(aiy.voicehat.LED.PULSE_SLOW)
    
    welcome_message = Text(app, text="Photo booth")
    #photo = Picture(app, image="test.jpg")
    
    
    button.on_press(button_take_photo)
    
    
    #button.wait_for_press()
    #led.set_state(aiy.voicehat.LED.BLINK_3)
    #time.sleep(2)
    #camera.capture('test.jpg')
    
    #camera.stop_preview()
    photo.image = 'test.jpg'
    
    app.display()
    
finally:
    camera.close()
