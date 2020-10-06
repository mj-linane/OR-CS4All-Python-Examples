import turtle
import random
wn = turtle.Screen()
wn.screensize(500, 500, 'black')
turtle = turtle.Turtle()

# Setup Turtle
turtle.pencolor('white')
turtle.pensize(1)
turtle.pu()

# Go to location and draw dot
turtle.goto(0, -100)
turtle.dot(100)

turtle.goto(0, 100)
turtle.dot(random.randint(1, 100))
turtle.goto(random.randint(0, 100), random.randint(0, 100))
turtle.dot(random.randint(50, 200))

# Made into a function


def draw_random_dot(size, x, y):
    turtle.goto(x, -y)
    turtle.dot(size)

    turtle.goto(x, -y)
    turtle.dot(size)

    turtle.goto(x, -y)
    turtle.dot(size)


# draw_random_dot(random.randint(0, 100), random.randint(
#     0, 300), random.randint(0, 300))

# draw_random_dot(random.randint(0, 100), random.randint(
#     0, 300), random.randint(0, 300))

# draw_random_dot(random.randint(0, 100), random.randint(
#     0, 300), random.randint(0, 300))

def draw_random_dots():
    for n in range(20):
        draw_random_dot(random.randint(0, 100), random.randint(
            0, 300), random.randint(0, 300))


wn.exitonclick()
