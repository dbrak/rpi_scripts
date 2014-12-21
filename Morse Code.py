#!/usr/bin/python

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

#define function to blink LEDs
def blink(x):
	GPIO.output(17, True)
	GPIO.output(27, True)
	GPIO.output(22, True)
	GPIO.output(25, True)
	GPIO.output(8, True)
	GPIO.output(7, True)
	time.sleep(x)
	GPIO.output(17, False)
	GPIO.output(27, False)
	GPIO.output(22, False)
	GPIO.output(25, False)
	GPIO.output(8, False)
	GPIO.output(7, False)
	time.sleep(.5)
	
#Get string to parse into morse code
morse_code = raw_input ('Enter a string of . and -:  ')

#loop to check for incorrect characters
i = 0
for i in range (len(morse_code)):
	if morse_code[i] != "." and morse_code[i] != "-":
		print ('Error - Use only + and -')
	elif morse_code[i] == '-' :
		blink(1)
	else :
		blink(.5)
	

