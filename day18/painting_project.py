# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
import turtle
from turtle import *
from random import choice
color_list=[(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
def random_color():
    random_color=choice(color_list)
    return random_color
test_turtle=Turtle()
test_turtle.hideturtle()
y=250
x=-250
turtle.colormode(255)
def set_position():
    global y
    y-=50
    return y
test_turtle.penup()
test_turtle.goto(x,y)

for i in range(10):
    for j in range(10):
        test_turtle.dot(20,random_color())
        test_turtle.penup()
        test_turtle.forward(50)
    test_turtle.goto(x,set_position())

Screen().exitonclick()