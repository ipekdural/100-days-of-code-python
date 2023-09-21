from turtle import Turtle,Screen

import pandas
screen=Screen()
screen.addshape("blank_states_img.gif")
screen.title("U.S. State Game")
state_turtle=Turtle()
state_turtle.shape("blank_states_img.gif")
pen=Turtle()
pen.hideturtle()
pen.penup()
pen.color("red")
answer_state=screen.textinput(title="Guess the State",prompt="What is another state's name?")
data=pandas.read_csv("50_states.csv")
# print(data)
correct=data[data.state==answer_state]
state_name=correct["state"].to_list()
x_location=correct["x"].to_list()
y_location=correct["y"].to_list()
pen.goto(x_location[0],y_location[0])
pen.write(f"{state_name[0]}",align="center",font=("Courier",8,"bold"))






screen.exitonclick()