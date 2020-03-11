import turtle
import random
wn = turtle.Screen()
wn.screensize(500, 500, 'black')
turtle = turtle.Turtle()

# Setup Turtle
turtle.pencolor('white')
turtle.pensize(1)
turtle.pu()


def draw_random_dot(size, x, y):
    turtle.goto(x, -y)
    turtle.dot(size)

    turtle.goto(x, -y)
    turtle.dot(size)

    turtle.goto(x, -y)
    turtle.dot(size)


def draw_random_dots():
    for n in range(20):
        draw_random_dot(random.randint(0, 100), random.randint(
            0, 300), random.randint(0, 300))


draw_random_dots()

wn.exitonclick()
