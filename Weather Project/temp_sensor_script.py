#!/usr/bin/env python

import time
import pigpio 
import sys
sys.path.append('/home/pi/PIGPIO')
import DHT22
import csv

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
	with open('temp_data.csv','a') as fp:
	    a = csv.writer(fp,delimiter-',')
	    data = [[time.strftime('%x'),time.strftime('%X'),h,t]]
	    fp.writerows(data)
	    fp.close()
	time.sleep(120)