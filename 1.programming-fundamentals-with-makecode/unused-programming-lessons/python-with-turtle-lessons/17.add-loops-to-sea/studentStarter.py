# SETUP CODE -- Don't Change
import turtle
import random

wn = turtle.Screen()  # Set up the window and its attributes
turtle = turtle.Turtle()  # Creates the turtle, named "turtle"

# CUSTOMIZE TURTLE -- Change With Caution
wn.bgcolor("blue")  # Sets color of the background
turtle.color("white")  # Sets color of the pen
turtle.pensize(5)  # Width of the pen
turtle.left(90)  # Sets turtle to start facing up
turtle.speed('fastest')  # Turtle drawing speed
turtle.tracer(0, 0)  # turns off the animation


# COMPLETE YOUR CODE Enter your code below


# To do: Repeatedly draw sea grass
def draw_all_seagrass():
    for n in range(5):
        turtle.goto(random.randint(0, 320), 0)
        turtle.setheading(0)
        draw_seagrass(random.randint(10, 60))


# To do: Repeatedly draw sea stars
def draw_all_seastars():
    for n in range(5):
        pass


# To do: Repeatedly draw fish


def draw_all_fish():
    for n in range(5):
        pass


# To do: Repeatedly draw bubbles


def draw_all_bubbles():
    for n in range(5):
        turtle.goto(random.randint(0, 320), random.randint(0, 450))
        draw_bubble(random.randint(1, 5))


# Draw a five-pointed star with a wide pen of the given size
def draw_seastar(size):
    turtle.pd()
    turtle.color(255, 0, 255)
    turtle.width(10)
    turtle.pd()
    turtle.setheading(0)
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
    turtle.right(144)

    turtle.pu()


# Switches between left and right arcs to make seaGrass with the given radius
def draw_seagrass(size):
    turtle.color(0, random.randint(150, 200), 0)
    turtle.width(3)
    turtle.pd()

    # Draw four arcs to make grass
    turtle.setheading(0)
    turtle.left(90)
    turtle.circle(size, 30)
    turtle.right(180)
    turtle.circle(size, -60)
    turtle.right(180)
    turtle.circle(size, 60)
    turtle.right(180)
    turtle.circle(size, -60)
    turtle.right(180)

    turtle.pu()


# Draws a fish at the current turtle location with the given size and color
def draw_fish(size, red, green, blue):
    turtle.color(red, green, blue)
    turtle.width(size)
    turtle.pd()

    # Fish body
    turtle.dot(size)
    turtle.setheading(0)
    turtle.forward(size)

    # Fish tail
    turtle.left(30)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)

    turtle.pu()


# Bubbles are turtle.dots
def draw_bubble(size):
    # turtle.color(100, 100, 255, .2)
    turtle.dot(size)


# These six defs draw everything. Order matters
# for how different parts of the picture are layered.
turtle.pu()
draw_all_seagrass()
draw_all_seastars()
draw_all_fish()
draw_all_bubbles()

# No animation -> Update updates the display when finished
turtle.update()
