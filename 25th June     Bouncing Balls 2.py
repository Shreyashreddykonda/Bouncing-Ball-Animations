import turtle
import math
import time

s1 = turtle.Screen()
s1.setup(800, 800)
s1.bgcolor("light green")

t1 = turtle.Turtle()
t1.color("orange")
t1.shape('circle')

tb = turtle.Turtle()
tb.pencolor("black")
tb.pensize(10)

t2 = turtle.Turtle()
t2.color("green")
t2.shape('circle')

t3 = turtle.Turtle()
t3.color("black")
t3.shape('circle')

t4 = turtle.Turtle()
t4.color("yellow")
t4.shape('circle')

tb = turtle.Turtle()
tb.pencolor("black")
tb.pensize(10)
tb.penup()
tb.goto(-300, 300)
tb.pendown()
tb.goto(300, 300)
tb.goto(300, -300)
tb.goto(-300, -300)
tb.goto(-300, 300)

x1 = 0
y1 = 0
dx1 = 0
dy1 = 5

x2 = 0
y2 = 0
dx2 = 5
dy2 = 5


x3 = 0
y3 = 0
dx3 = 5
dy3 = 0

x4 = 0
y4 = 0
dx4 = 5
dy4 = -5

t1.goto(x1, y1)
t2.goto(x2, y2)
t3.goto(x3, y3)
t4.goto(x4, y4)

while True:
    t1.penup()
    t1.goto(x1, y1)
    t1.pendown()

    x1 = x1 + dx1
    y1 = y1 + dy1

    if(y1 > 300):
        dy1 = -5
    if(y1 < -300):
        dy1 = 5
        
    t2.penup()
    t2.goto(x2, y2)
    t2.pendown()

    x2 = x2 + dx2
    y2 = y2 + dy2

    if(x2 > 300):
        dy2 = -5
        dx2 = -5
    if(x2 < -300):
        dy2 = 5
        dx2 = 5

    t3.penup()
    t3.goto(x3, y3)
    t3.pendown()
    
    x3 = x3 + dx3
    y3 = y3 + dy3
    
    if(x3 > 300):
        dy3 = 0
        dx3 = -5
    if(x3 < -300):
        dy3 = 0
        dx3 = 5

    t4.penup()
    t4.goto(x4, y4)
    t4.pendown()
    
    x4 = x4 + dx4
    y4 = y4 + dy4
    
    if(x4 > 300):
        dy4 = 5
        dx4 = -5
    if(x4 < -300):
        dy4 = -5
        dx4 = 5
