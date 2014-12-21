#!/usr/bin/env python

import turtle
import math


sides = input("Enter an integer for the number of sides in between 1 and 360: ")
while sides < 1 or sides > 360:
    sides = input("Try again:  ")

angle = (360/sides)
per = 0

length = input("Enter an integer for the length in between 1 and 200: ")
while length < 1 or length > 200:
    length = input("Try again: ")


wn = turtle.Screen()
wn.bgcolor("green")
wn.title("Polygon")

t = turtle.Pen()
t.pensize(3)
t.color("blue")
t.speed(6)


for i in range(sides):
    t.forward(length)
    t.left(angle)
    per = per + length

area = (per/2)*(length/(2*math.tan(math.radians(180/sides))))



tu = turtle.Pen()
tu.pensize(3)
tu.color("blue")
tu.ht()
tu.up()
tu.goto(0,-30)
tu.write ("The perimeter is " + str(per))
tu.goto(0,-40)
tu.write ("The angle is " + str(180 - angle))
tu.goto(0,-50)
tu.write ("The area is " + str(area))


turtle.done()
    
