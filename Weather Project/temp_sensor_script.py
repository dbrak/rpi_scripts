#!/usr/bin/env python

import time
import pigpio 
import sys
sys.path.append('/home/pi/PIGPIO')
import DHT22
import cvs

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
	 
    #Write to file
    with open('temp_data.csv','a') as file:
        a = csv.writer(file,delimiter=',');
        data = [[time.strftime('%x'),time.strftime('%X'),h,t]];        
        file.writerows(data)
        file.close()

    time.sleep(120)

 
 
 
 
 
 
 