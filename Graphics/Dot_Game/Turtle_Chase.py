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
wn.title(" Turtle_Chase")

t2 = turtle.Turtle() 
t2.pensize(5
)
t2.speed(10)
t2.color('red')
t2.shape("circle")
t2.goto(-100,-100)
	
t3 = t2.clone()



x = input ("Select a number.")
y = input ("Select another number.") 
t.goto(y,x)
print("Let The Chase Begin!")



def number_set():
   o = random.randrange(0,100)
   return o


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
   
     

class Turtle:
	def follow(turtle):
		pos = t.position(turtle)
   		angle = t2.towards(pos)
   		fward = number_set()   	
   		t2.setheading(angle)
		t2.forward(fward)
		distance = t2.distance(t)
		print(distance)  
		if (15.0 >= distance >= -15.0) :
			t2.write("Ha Ha Gotcha! You are Pesky Turtle! Ha Ha ",font=("Comic Sans NS", 15, "normal"))
		


def setup():
	wn.onkey(forward,"Up")
	wn.onkey(right,"Right")
	wn.onkey(left,"Left")
	wn.onkey(backward,"Down")
	wn.onkey(setup,"space")
   	wn.listen()	   
   
setup()






turtle.done()