import turtle
from turtle import *
import random

turtle.colormode(255)


def rand_color_gen():
    r = random.randint(0, 255)  # Generate a random value between 0 and 1
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


my_screen = Screen()
trtle = Turtle()
turn = 3
angle = 120
trtle.hideturtle()
trtle.penup()
trtle.goto(-200, 200)
trtle.showturtle()
trtle.pendown()

while turn < 11:
    trtle.pencolor(rand_color_gen())
    for i in range(turn):
        trtle.forward(100)
        trtle.right(angle)
    turn += 1
    angle = 360 / turn

my_screen.exitonclick()
