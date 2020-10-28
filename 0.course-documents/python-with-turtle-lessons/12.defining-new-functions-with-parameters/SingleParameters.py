import turtle
wn = turtle.Screen()

wn.bgcolor('black')

turtle = turtle.Turtle()
turtle.color('white')


# def shape():
#   turtle.fd(100)
#   turtle.left(90)
#   turtle.fd(100)

def shape(length):
    turtle.fd(length)
    turtle.left(90)
    turtle.fd(length)


shape(100)
turtle.pu()
turtle.goto(200, 200)
turtle.pd()
shape(200)

wn.exitonclick()  # leaves window open until I click on it
