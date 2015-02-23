#!/usr/bin/env python

import turtle
import math

num = raw_input("How many squares do you want?")
length = 100
angle = 360 / int(num)


wn = turtle.Screen()
wn.bgcolor("green")
wn.title("Spiral")

t = turtle.Pen()
t.pensize(2)
t.color("blue")
t.speed(60)



def square():
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)

for x in range (0,int(num)+1):
    square()
    t.left(angle)

turtle.done()
    
