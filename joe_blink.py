#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import picamera

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Setup GPIO pins
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

#define function to all blink LEDs
def blinkall(delay):
	GPIO.output(17, True)
	GPIO.output(27, True)
	GPIO.output(22, True)
	GPIO.output(25, True)
	GPIO.output(8, True)
	GPIO.output(7, True)
	time.sleep(delay)
	GPIO.output(17, False)
	GPIO.output(27, False)
	GPIO.output(22, False)
	GPIO.output(25, False)
	GPIO.output(8, False)
	GPIO.output(7, False)
	
#define function to blink a specific LED
def blink(pin,delay):
	GPIO.output(pin, True)
	time.sleep(delay)
	GPIO.output(pin, False)
	
#Joe to insert code here)
def hublub():
        blinkall(.01)
        blink (7,1)
        blink (8,1)
        blink (7,2)
        blink (8,2)
        blink (7,3)
        blink (8,3)
        blink (7,4)
        blink (8,4)
        blink (7,5)
        blink (8,5)
        blinkall(6)

#hublub()

def picam(delay):
       camera = picamera.PiCamera()
       camera.start_preview()
       camera.vflip = True
       time.sleep(delay)
       camera.stop_preview()
       camera.close()

picam(5)               

GPIO.cleanup()
	

