import time
import turtle
import random


bg = turtle.Screen()
bg.bgcolor("magenta")


turtle.penup()
turtle.goto(-170,-180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)


turtle.penup()
turtle.goto(-160,-150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)


turtle.penup()
turtle.goto(-150,-120)
turtle.color("white")
turtle.pendown()
turtle.forward(250)


turtle.penup()
turtle.goto(-100,-100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()


turtle.penup()
turtle.goto(-90,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-60,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-30,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(0,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(30,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)


colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)


turtle.penup()
turtle.goto(-150, 50)
turtle.color("yellow")
turtle.pendown()
turtle.write("Happy Birthday Nahid Bhrata!!!!",font=("arial",20,"italic"))
turtle.color("black")
time.sleep(10)