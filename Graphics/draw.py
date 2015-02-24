#!/usr/bin/env python

import turtle
import math
import random

length = 100
colorlist = ['red','blue','white','yellow','green']


t = turtle.Pen()
t.pensize(2)
t.speed(60)

def set_color():
    i = random.randrange(0,5)
    return colorlist[i]

def square():
    t.color(set_color())
    t.fillcolor(set_color())
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
    wn.bgcolor("black")
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
    
