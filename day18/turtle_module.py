from turtle import Turtle, Screen

my_screen = Screen()
# test_turtle = Turtle()
# for _ in range(4):
#     test_turtle.forward(100)
#     test_turtle.right(90)

##############################################################
# Aliasing modules
import random as r
random_number = r.randint(1, 10)
############################################################
test_turtle2=Turtle()
test_turtle2.hideturtle()
test_turtle2.penup()
test_turtle2.goto(-300,300)
test_turtle2.showturtle()
test_turtle2.pendown()

for _ in range(30):
    test_turtle2.penup()
    test_turtle2.forward(10)
    test_turtle2.pendown()
    test_turtle2.forward(10)


my_screen.exitonclick()