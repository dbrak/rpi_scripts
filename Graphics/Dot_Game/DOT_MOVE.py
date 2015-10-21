#!/usr/bin/env python

import time
import turtle

t = turtle.Pen()
t = turtle.Pen() 
t.pensize(4)
t.speed(0)
t.hideturtle()
t.color('red')

wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("DOT_MOVE")

def md():
   t.up()
   t.goto(61,70)
   t.down()
   t.dot()
   time.sleep(5)
   t.undo()
   t.up()
   t.goto(10,39)
   t.down()
   t.dot()
	

md()  
   
turtle.done()
   