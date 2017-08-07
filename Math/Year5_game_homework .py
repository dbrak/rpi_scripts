from random import randint

score = 0
target = input ("What do you want your target number to be? ")
max = input ("What do you want your top times table to be? " )

while (score < target):

	num1 = randint(0,max)
	num2 = randint(0,12)
	
	qu = input ("what is %d x %d = " %(num1,num2))
	
	if (qu == num1 * num2):
		score = score + 5
		print "You currently have %d" % score 
	else:
		score = score - 3
		print "You currently have %d" % score 