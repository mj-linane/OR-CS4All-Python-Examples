# SETUP CODE -- Don't Change
import turtle
wn = turtle.Screen()  # Set up the window and its attributes
turtle = turtle.Turtle()  # Creates the turtle, named "turtle"

# CUSTOMIZE TURTLE -- Change With Caution
wn.bgcolor("black")  # Sets color of the background
turtle.color("white")  # Sets color of the pen
turtle.pensize(5)  # Width of the pen
turtle.left(90)  # Sets turtle to start facing up
turtle.speed(10)  # Turtle drawing speed

# COMPLETE YOUR CODE Enter your code below

# Setup mini programs


def step():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)


def side():
    step()
    step()
    step()
    turtle.forward(100)
    turtle.right(90)


# Draw shape
side()
side()
side()
side()
