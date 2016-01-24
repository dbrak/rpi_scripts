#!/usr/bin/env python

import time
import pigpio 
import sys
sys.path.append('/home/pi/PIGPIO')
import DHT22

#instantiate pi and sensor objects
pi = pigpio.pi()
s = DHT22.sensor(pi,4)

#Take reading and write values to varible
s.trigger()
h = s.humidity()
t = s.temperature()

#Write to file
file = open('temp_data.csv','a')
file.write(h,t)
file.close()

 
 
 
 
 
 
 #time.sleep(300)
 