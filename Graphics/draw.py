#!/usr/bin/env python

import turtle
import math
import random

length = 100
colorlist = ['red','blue','white','yellow']


t = turtle.Pen()
t.pensize(2)
t.speed(60)



     
     
def set_color():
    i = random.randrange(0,4)
    return colorlist[i]

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

def strait():
    t.forward(50)
    
def hexaflower():
    for x in range(0,10):   
        hexagon()
        t.left(36)

def octogon():
    for x in range (0,8):
        t.forward(length)
        t.left(360/8)
    

def spiderweb():
    octogon(50)
    t.goto(10,4)
    t.forward(20)
    octogon(100)

def roadtracks():
    for x in range(0,15):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()





def right():
    t.right(90)

def left():
    t.left(90)

def setup():    
    wn.reset()
    wn.bgcolor("green")
    wn.title("Draw")
    wn.onkey(roadtracks,'r')
    wn.onkey(left,"Left")
    wn.onkey(right,"Right")
    wn.onkey(octogon,'8')
    wn.onkey(hexagon,'6')    
    wn.onkey(pendown,'d')        
    wn.onkey(penup,'u')
    wn.onkey(square,'4')
    wn.onkey(flower,'f')
    wn.onkey(strait, "Up")
    wn.onkey(hexaflower,'t')
    wn.onkey(setup,'c')
    wn.listen() 


wn = turtle.Screen()

setup()

turtle.done()
    
