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

preview_mode = False

app = App(title="Camera")

img = ImageTk.PhotoImage(Image.open('test.jpg'))
preview = Text(app, text="Preview")
preview.tk.config(image = img)


def button_take_photo():
    global preview_mode
    if preview_mode == True:
        led.set_state(aiy.voicehat.LED.BLINK_3)
        time.sleep(2)
        camera.capture('test.jpg')
        led.set_state(aiy.voicehat.LED.PULSE_SLOW)
        camera.stop_preview()
        img = ImageTk.PhotoImage(Image.open('test.jpg'))
        preview.tk.config(image = img)
        preview_mode = False
    else:
        camera.start_preview()
        preview_mode = True




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
