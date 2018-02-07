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

app = App(title="Camera", height=768, width=1024)

countdown = Text(app, text="Countdown")

img = ImageTk.PhotoImage(Image.open('test.jpg'))
preview = Text(app, text="Preview")
preview.tk.config(image = img)


def button_take_photo():
    global preview_mode
    if preview_mode == True:
        led.set_state(aiy.voicehat.LED.BLINK_3)
        countdown.text = 'Photo in 3, 2, 1'
        
        time.sleep(2)
        
        camera.stop_preview()
        camera.resolution = (1280, 720)
        camera.capture('test.jpg')
        led.set_state(aiy.voicehat.LED.PULSE_SLOW)
        
        img = ImageTk.PhotoImage(Image.open('test.jpg').resize((640, 360)))
        preview.tk.config(image = img)
        preview.image = img
        
        preview_mode = False
    else:
        camera.resolution = (640, 360)
        camera.start_preview()
        camera.preview.window = (192, 100, 640, 360)
        
        img = ImageTk.PhotoImage(Image.open('background.jpg'))
        preview.tk.config(image = img)
        preview.image = img
        
        preview_mode = True




camera = picamera.PiCamera()
camera.rotation = 180
camera.preview_fullscreen = False


try:
    
    led.set_state(aiy.voicehat.LED.PULSE_SLOW)
    
    welcome_message = Text(app, text="Photo booth")
    
    
    button.on_press(button_take_photo)

    
    app.display()
    
finally:
    camera.close()
