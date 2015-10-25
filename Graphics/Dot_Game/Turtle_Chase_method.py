#!/usr/bin/env python


import random 
import time
import turtle

d = 80

t = turtle.Turtle() 
t.pensize(10)
t.speed(0)
t.color('blue')
t.shape("turtle")

wn = turtle.Screen()
wn.bgcolor("black")
#wn.title(" ")

t2 = turtle.Turtle() 
t2.pensize(10)
t2.speed(10)
t2.color('red')
t2.shape("circle")
t2.goto(-100,-100)
	
t3 = t2.clone()



x = input ("Select a number.")
y = input ("Select another number.") 
t.goto(y,x)
print("Let The Chase Begin!")

class Turtle:
	def follow(self,target):
		pos = target.position()
   		angle = self.towards(pos)
   		fward = random.randrange(0,100)
   		self.setheading(angle)
		self.forward(fward)
		distance = t2.distance(t)
		print(distance)  
		if (15.0 >= distance >= -15.0) :
		#self.write("Ha Ha Gotcha! You are Pesky Turtle! Ha Ha Ha Ha",font=("impact", 15, "normal"))
		#self.write("Press space to play agen.",font=("Arial Black", 15, "normal"))\

def forward():
  t.up()
  t.forward(d)
  t2.follow()
 
def right():
  t.up()
  t.right(90)
  t.forward(d)
  t2.follow()
  
def left():
  t.up()
  t.left(90)
  t.forward(d)
  t2.follow()
  
def backward():
   t.up()
   t.right(180)
   t.forward(d)
   t2.follow()
   


def setup():
	wn.onkey(forward,"Up")
	wn.onkey(right,"Right")
	wn.onkey(left,"Left")
	wn.onkey(backward,"Down")
	wn.onkey(setup,"space")
   	wn.listen()	   
   
setup()






turtle.done()