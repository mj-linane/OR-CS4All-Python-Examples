import turtle
wn = turtle.Screen()
turtle = turtle.Turtle()

# turtle.dot(100, 'blue')

#turtle.circle(100, 180)
#turtle.circle(-100, 180)

turtle.forward(50)
print(turtle.position())
turtle.goto(100, 100)
turtle.forward(50)

turtle.setheading(45)
turtle.forward(50)

turtle.penup()
turtle.home()
turtle.pendown()
turtle.forward(100)
