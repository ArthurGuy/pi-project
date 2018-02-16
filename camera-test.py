import time
import picamera

# export DISPLAY=:0.0


while True:
    
    camera = picamera.PiCamera()
    camera.rotation = 0
    camera.preview_fullscreen = False

    camera.resolution = (640, 360)
    camera.start_preview()
    camera.preview.window = (192, 100, 640, 360)
    

camera.close()
