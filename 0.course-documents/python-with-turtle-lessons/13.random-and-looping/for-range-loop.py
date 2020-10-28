# Drawing In Random Locations Example

import turtle
import random

wn = turtle.Screen()
wn.screensize(500, 500, 'black')
turtle = turtle.Turtle()
turtle.pencolor('white')
turtle.pensize(1)


def draw_dot():
    turtle.pu()
    turtle.goto(0, -100)
    turtle.pd()
    turtle.dot(50, 'white')


def draw_random_dot():
    turtle.pu()
    turtle.goto(random.range(300), random.range(300))
    turtle.pd()
    turtle.dot(50, 'white')


def draw_square():
    turtle.left(25)
    turtle.forward(150)
    turtle.left(50)
    turtle.forward(50)


def draw_random_square():
    turtle.pu()
    turtle.goto(random.range(300), random.range(300))
    turtle.pd()
    draw_square()


# Main Drawing Loop
for n in range(100):
    # Add any of the functions to this loop to do that action 100 times
    draw_random_dot()


wn.exitonclick()  # leaves window open until I click on it
