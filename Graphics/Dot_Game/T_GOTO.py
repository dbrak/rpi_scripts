#!/usr/bin/env python

import random
import turtle

t = turtle.Pen() 
t.pensize(4)
t.speed(0)
t.color('white')
t.shape("turtle")

#Add a second turtle named t2 and change its color and shape as you like


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("T_GOTO")

for i in range (0,4): 
	x = input ("Select a number.")
	y = input ("Select another number.") 
	t.pendown()
	t.goto(y,x)
#use .towards to point the second turtle at the first turtle and .forward to move him 25 every time the loop runs


turtle.done()