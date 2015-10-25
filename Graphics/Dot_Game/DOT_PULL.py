#!/usr/bin/env python


import random 
import time
import turtle

d = 80


t = turtle.Turtle() 
t.pensize(4)
t.speed(0)
t.color('blue')
t.shape("turtle")


t2 = turtle.Turtle() 
t2.pensize(4)
t2.speed(10)
t2.color('red')
t2.shape("turtle")


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("DOT_PULL")


def number_set():
   o = random.randrange(0,100)
   return o


def forward():
  t.up()
  t.forward(d)
  follow()
 
def right():
  t.up()
  t.right(90)
  t.forward(d)
  follow()
  
def left():
  t.up()
  t.left(90)
  t.forward(d)
  follow()
  
def backward():
   t.up()
   t.right(180)
   t.forward(d)
   follow()
   
     
def follow():
	pos = t.position()
   	angle = t2.towards(pos)
   	fward = number_set()   	
   	t2.setheading(angle)
	t2.forward(fward)
	distance = t2.distance(t)
	print(distance)  
	if (30.0 >= distance >= -30.0) :
		print("Gotcha!")
		wn.clear


def setup():
	wn.onkey(forward,"Up")
	wn.onkey(right,"Right")
	wn.onkey(left,"Left")
	wn.onkey(backward,"Down")
	wn.onkey(setup,"0")
   	wn.listen()	   
   
setup()

turtle.done()

 