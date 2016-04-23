#!/usr/bin/env python

from random import randint

s = 0
comp_s = 0
print "----------"
 

for i in range(1,100):


	x = randint(1,8)
	print "Your integer is %d" % x 

	count = 0
	while(count<3):
		sq = input("What is your number squared:  ") 

		if sq == x*x:
			print "Correct"
			break
		else:
			print "Wrong, Try Again"
			count += 1
	else: 
		print "Sorry, too many tries.  You lose!"


	count = 0
	while(count<3):
		sc = input("Your last score was %d. What is your new one:  " % s) 

		if sc == s + sq:
			print "Correct"
			s += sq
			break
		else:
			print "Wrong, Try Again"
			count += 1
	else: 
		print "Sorry, too many tries.  You lose!"

	if s >= 100:
		print "----------"	
		print "You won!!!"
		print "----------"		
		break

	x = randint(1,8) 	
	print "----------"	
	print "My Turn"
	print "My number is %d." % x 
	print "It's square is %d" % (x*x)
	comp_s += x*x
	print "My score is %d" % comp_s
	print "----------"
	
	if comp_s >= 100:
		print "----------"	
		print "I won!!!"
		print "Too bad!  Try again."
		print "----------"
		break 
	
	