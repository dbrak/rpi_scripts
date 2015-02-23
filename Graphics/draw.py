#!/usr/bin/env python

import turtle
import math

length = 100
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

def flower():
    for x in range(0,10):
        square()
        t.left(36)

def penup():
    t.penup()

def pendown():
    t.pendown()

def hexagon():
    for x in range (0,6):
        t.forward(length)
        t.left(360 / 6)

def up():
    t.forward(50)


def hexaflower():
    for x in range(0,10):
        hexagon()
        t.left(36)

def setup():    
    wn.reset()
    wn.bgcolor("green")
    wn.title("Draw")
    wn.onkey(hexagon,'h')    
    wn.onkey(pendown,'d')        
    wn.onkey(penup,'u')
    wn.onkey(square,'s')
    wn.onkey(flower,'f')
    wn.onkey(up, "Up")
    wn.onkey(hexaflower,'t')
    wn.onkey(setup,'c')
    wn.listen() 


wn = turtle.Screen()
    
setup()

turtle.done()
    
