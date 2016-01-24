#!/usr/bin/env python

import random
import turtle

t = turtle.Pen() 
t.pensize(4)
t.speed(0)
t.hideturtle()
t.color('blue')

wn = turtle.Screen()
wn.bgcolor("red")
wn.title("DOT_MAKER")



def number_set():
   g = random.randrange(-300,300)
   return g

for i in range(0,300):
   x = number_set()
   y = number_set()
   t.up()
   t.goto(x,y)
   t.down()
   t.dot()
   
turtle.done()

   
   