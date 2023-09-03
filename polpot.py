import turtle
import time

t = turtle.Turtle()
t.speed(100)
t.penup()
t.goto(-300, 200)
t.pendown()
t.color("red")

# 绘制国旗矩形
t.begin_fill()
for _ in range(2):
    t.forward(560)
    t.right(90)
    t.forward(280)
    t.right(90)
t.end_fill()

t.color("yellow")
t.begin_fill()
t.penup()
t.goto(-100, 0)
t.pendown()
t.left(90)
t.forward(10)
t.right(90)
t.forward(10)
t.left(90)
t.forward(9)
t.right(90)
t.forward(12)
t.left(90)
t.forward(30)
t.right(90)
t.forward(5)
t.left(180)

t.setheading(90)
a=3
for i in range(59):                
    if 0<=i<30:
        a=a-0.12
        t.rt(3)
        t.fd(a)
    else:
        a=a+0.12
        t.rt(3)
        t.fd(a)

t.setheading(90)
a=6
for i in range(59):                
    if 0<=i<30:
        a=a-0.24
        t.rt(3)
        t.fd(a)
    else:
        a=a+0.24
        t.rt(3)
        t.fd(a)

t.setheading(90)
a=3
for i in range(59):                
    if 0<=i<30:
        a=a-0.12
        t.rt(3)
        t.fd(a)
    else:
        a=a+0.12
        t.rt(3)
        t.fd(a)

t.setheading(0)
t.forward(5)
t.right(90)
t.forward(30)
t.left(90)

t.forward(12)
t.right(90)
t.forward(9)
t.left(90)
t.forward(10)
t.right(90)
t.forward(10)
t.right(90)
t.forward(165)
t.end_fill()

t.color("red")
t.begin_fill()
for _ in range(2):
    t.forward(180)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

t.right(90)
t.penup()
t.goto(-100, 0)
t.pendown()
t.color("yellow")
t.begin_fill()
for _ in range(2):
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.right(90)
t.end_fill()

input()