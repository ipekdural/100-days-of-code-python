from turtle import Turtle, Screen
from random import randint, choice

colors = ["red", "green", "blue", "yellow", "orange", "purple"]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Who will win? Choose a color:")
i = 0
turtles = []
for y in range(-100, 101, 40):
    turtle = Turtle(shape="turtle")
    turtles.append(turtle)
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(-230, y)
    i += 1
is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle_x = turtle.xcor()
        if turtle_x >= 220:
            is_race_on = False
            winner_turtle=turtle.pencolor()
            if user_bet==winner_turtle:
                print(f"You've won! The winning color is {winner_turtle}")
            else:
                print(f"You've lost! The winning color is {winner_turtle}")


        step = randint(0, 10)
        turtle.forward(step)

screen.exitonclick()
