#!/usr/bin/env python

import turtle
import random

t = turtle.Pen() 
t.pensize(100)
t.speed(10)

wn = turtle.Screen()

colorlist = ['red','blue','green','purple','black','yellow','gray']    

def set_color():
    i = random.randrange(0,7)
    return colorlist[i]



def Square():
   for x in range(0,4):
     t.forward(100)
     t.right(90)
   

def CS():
   for x in range(0,8):
     color = set_color()
     t.color(color)
     t.circle(50)
     t. right(40)
   
   
def CSS():
   for x in range (0,10):
      color = set_color()
      color2 = set_color()      
      t.color(color) 
      t.circle(50)
      t.color(color2)       
      t.right(36)
      Square()
      
def setup():  
	wn.reset()
	wn.bgcolor("orange")
	wn.title("Spiral 2.0")
	wn.onkey(CS,'1')   
	wn.onkey(CSS,'2')
	wn.onkey(setup,'s') 
	wn.listen()


setup()


turtle.done()  
   