import turtle
wn = turtle.Screen()

wn.bgcolor("green")
t = turtle.Pen()

per = 0
length = 12
width = 5
area = 0

t.forward(length)
per = per + length
t.left(90)
t.forward(width)
per = per + width
t.left(90)
t.forward(length)
per = per + length
t.left(90)
t.forward(width)
per = per + width
t.left(90)
area = length * width

print("The area is " + str(area))
print("The perimeter is " + str(per))

turtle.done()

