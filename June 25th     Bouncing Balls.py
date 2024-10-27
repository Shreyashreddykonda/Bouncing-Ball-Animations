import turtle
import math
import time

s1 = turtle.Screen()
s1.setup(800, 800)
s1.bgcolor("light green")

t1 = turtle.Turtle()
t1.color("blue")
t1.shape('circle')
t1.goto(0, 0)

t3 = turtle.Turtle()
t3.color("orange")
t3.shape('circle')
t3.goto(0, 0)

ts = turtle.Turtle()
ts.pencolor("brown")
ts.penup()
ts.pensize(5)

ts.goto(-300, 300)
ts.pendown()
ts.goto(300, 300)
ts.goto(300, -300)
ts.goto(-300, -300)
ts.goto(-300, 300)

x1 = 0
y1 = 0
dx1 = 10
dy1 = 0
x3 = 0
y3 = 0
dx3 = 0
dy3 = 0

while True:
    t1.penup()
    t1.goto(x1, y1)
    t1.pendown()
    
    t3.penup()
    t3.goto(x3, y3)
    t3.pendown()

    time.sleep(0.1)
    if(x1 > 300):
        dx1 = -5
    if(x1 < -300):
        dx1 = 5

    x1 = x1 + dx1
    y1 = y1 + 0

    if(y3 > 300):
        dy2 = -5
    if(y3 < -300):
        dy2 = 5

    x3 = x3 + 0
    y3 = y3 + dy3
