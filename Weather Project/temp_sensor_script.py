#!/usr/bin/env python

import time
import pigpio 
import sys
sys.path.append('/home/pi/PIGPIO')
import DHT22

#instantiate pi and sensor objects
pi = pigpio.pi()
s = DHT22.sensor(pi,4)

#Take reading and write values to variable
for x in range (0,5):
	s.trigger()
	h = s.humidity()
	t = s.temperature()
	print(h)
	print(t)
	time.sleep(120)
 





#Write to file
#file = open('temp_data.csv','a')
#file.write(t)
#file.close()

 
 
 
 
 
 
 