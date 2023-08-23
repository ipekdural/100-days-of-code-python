# from turtle import Turtle,Screen
# test = Turtle()
# my_screen = Screen()
# test.shape("turtle")
# test.color("#5C8374")
#
# print(my_screen.canvheight)
# test.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
#using methods
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

#change attribute accesing fields
table.align="r"
print(table)
