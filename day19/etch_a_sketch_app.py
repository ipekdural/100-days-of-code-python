from turtle import Turtle, Screen
import random
import turtle
tim = Turtle()
screen = Screen()
turtle.colormode(255)
tim.pensize(2)
def rand_color_gen():
    r = random.randint(0, 255)  # Generate a random value between 0 and 1
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def W():
    tim.color(rand_color_gen())
    tim.forward(10)


def S():
    tim.color(rand_color_gen())
    tim.backward(10)


def A():
    tim.color(rand_color_gen())
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def D():
    tim.color(rand_color_gen())
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(W, "w")
screen.onkey(S, "s")
screen.onkey(A, "a")
screen.onkey(D, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()
