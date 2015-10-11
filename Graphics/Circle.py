#!/usr/bin/env python

import turtle 

wn = turtle.Screen()
wn.bgcolor("red")
wn.title("Circle")

t = turtle.Pen()
t.pensize(3)
t.color("pink")
t.speed(6)

x = input("Where do you want your circle to be on the x axis?  ")
y = input ("Where do you want your circle to be on the y axis?  ")
r = input ("Pick a number for your radius.  ")


t.penup()
t.goto(x,y)
t.pendown()
t.circle(r)

turtle.done()
 


 