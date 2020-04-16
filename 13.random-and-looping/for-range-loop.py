import turtle
import random
wn = turtle.Screen()
wn.screensize(500, 500, 'black')
turtle = turtle.Turtle()
turtle.pencolor('white')
turtle.pensize(1)

turtle.pu()
turtle.goto(0, -100)
turtle.pd()


for n in range(100):
    turtle.left(25)
    turtle.forward(150)
    turtle.left(50)
    turtle.forward(50)

wn.exitonclick()  # leaves window open until I click on it
