import random
import turtle
from turtle import Turtle,Screen
tim=Turtle()
my_screen=Screen()
########### Challenge 4 - Random Walk ########
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b
directions=[0,90,180,270]
tim.pensize(15)
tim.hideturtle()
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
    speed=5
    tim.speed(speed)
    speed+=20


