#!/usr/bin/env python

import time
import picamera

camera = picamera.PiCamera()

try:
        camera.start_preview()
        camera.vflip = True
        time.sleep(5)
        camera.stop_preview()
        camera.capture('Pic1.jpg') 
finally:
        camera.close()

        
        
