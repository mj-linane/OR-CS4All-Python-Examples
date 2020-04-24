# For Loop

import turtle
sn = turtle.Screen()
turtle = turtle.Turtle()
sn.bgcolor("black")
turtle.color("white")
turtle.speed("fast")


def square():
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)


def draw_all_squares():
    # For Loop
    for n in range(100):
        square()
        turtle.right(5)


draw_all_squares()
