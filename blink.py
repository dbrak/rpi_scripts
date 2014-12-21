#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

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
blink(8,7)
blink (7,6)
blink (22,5)
blink (17,4)
blink (25,3)
blink (27,2)
blinkall(1)
blink (7,1)
blink (8,1)
blink (17,1)
blink (22,1)
blink (25,1)
blink (27,1)
blinkall(4)


GPIO.cleanup()
	

