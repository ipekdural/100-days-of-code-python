import turtle
from turtle import *
from random import randint

test_turtle = Turtle()
heading_angle = 2
test_turtle.pensize(1)
turtle.colormode(255)
test_turtle.hideturtle()
test_turtle.speed('fastest')


def turn_times():
    n = int(360 / heading_angle)
    return n


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


for _ in range(turn_times()):
    test_turtle.color(random_color())
    test_turtle.right(heading_angle)
    test_turtle.circle(100)

Screen().exitonclick()