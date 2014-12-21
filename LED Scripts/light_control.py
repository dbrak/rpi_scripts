#! /usr/bin/python

import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

# North set of traffic light
# Define LED colour and their GPIO pin
RED_NORTH = 17
YEL_NORTH = 27
GRN_NORTH = 22

# East set of traffic light
RED_EAST = 25
YEL_EAST = 8
GRN_EAST = 7

GPIO.setmode(GPIO.BCM)

# Setup GPIO pins
GPIO.setup(RED_NORTH, GPIO.OUT)
GPIO.setup(YEL_NORTH, GPIO.OUT)
GPIO.setup(GRN_NORTH, GPIO.OUT)

GPIO.setup(RED_EAST, GPIO.OUT)
GPIO.setup(YEL_EAST, GPIO.OUT)
GPIO.setup(GRN_EAST, GPIO.OUT)

delay = 7
delay2 = 7


def light_control():
	loop = True
	while loop :
		control = raw_input('What color should we light (G,A,R)?')
		control = control.upper()
		if control == 'G' :
			print 'Green North Powering Up!'
			GPIO.output(GRN_NORTH, True)
			time.sleep (delay)
			print 'Green Powering Down!'
			GPIO.output(GRN_NORTH,False)		
			print 'Green East Powering Up!'
			GPIO.output(GRN_EAST,True)
                        time.sleep (delay2)
			print 'Green Powering Down!'
			GPIO.output(GRN_EAST,False)
		if control == 'A' :
			print 'Amber Powering Up!'
			GPIO.output(YEL_NORTH, True)
			GPIO.output(YEL_EAST,True)
			time.sleep (delay)
			print 'Amber Powering Down!'
			GPIO.output(YEL_EAST,False)
			GPIO.output(YEL_NORTH,False)
		if control == 'R' :
			print 'Red Powering Up!'
			GPIO.output(RED_NORTH, True)
			GPIO.output(RED_EAST,True)
			time.sleep (delay)
			print 'Red Powering Down!'
			GPIO.output(RED_EAST,False)
			GPIO.output(RED_NORTH,False)
		done = raw_input ('Are you done? (Y/N)')
		if done.upper() == 'Y' :
			loop = False		
    
light_control()
