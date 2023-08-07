import random

random_int = random.randint(1, 10)  # creating random int numbers
print(random_int)
random_float = (
    random.random()
)  # creating random float numbers between 0 and 1 (1 is not include)
print(random_float)
print(random_float * 5)  # creating random float between 0 and 5 (not inculind 5)


# List
states_of_america = [
    "Delaware",
    "Pennsylvania",
    "New Jersey",
    "Georgia",
    "Connecticut",
    "Massachusetts",
    "Maryland",
    "South Carolina",
    "New Hampshire",
    "Virginia",
    "New York",
    "North Carolina",
    "Rhode Island",
    "Vermont",
    "Kentucky",
    "Tennessee",
    "Ohio",
    "Louisiana",
    "Indiana",
    "Mississippi",
    "Illinois",
    "Alabama",
    "Maine",
    "Missouri",
    "Arkansas",
    "Michigan",
    "Florida",
    "Texas",
    "Iowa",
    "Wisconsin",
    "California",
    "Minnesota",
    "Oregon",
    "Kansas",
    "West Virginia",
    "Nevada",
    "Nebraska",
    "Colorado",
    "North Dakota",
    "South Dakota",
    "Montana",
    "Washington",
    "Idaho",
    "Wyoming",
    "Utah",
    "Oklahoma",
    "New Mexico",
    "Arizona",
    "Alaska",
    "Hawaii",
]

print(states_of_america[5])  # print the 6. index
print(states_of_america[-1])  # print the 1. index from end
states_of_america[1] = "Pencilvania"  # changin value
print(states_of_america[1])
states_of_america.append("ExampleCity")  # Adding an item end of the list
print(states_of_america[-1])
states_of_america.extend(["City1", "City2", "City3"])  # Adding list to actual list
print(states_of_america)


# Banker Roulette
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
import random

x = len(names)
choosen = random.randint(0, x - 1)
print(f"{names[choosen]} is going to buy the meal today!")


# Nested List
numbers = [1, 2, 3, 4, 5]
names = ["Angela", "Olric", "Karl", "Amy"]
mix_list = [numbers + names]
print(mix_list)


# Treasure Map
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input(
    "Where do you want to put the treasure?(column 2, row 3 would be entered as:23) "
)
column = int(position[0])
row = int(position[1])
map[row - 1][column - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")



# Rock, Paper, Scissors 
import random

rock = """
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random

images = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

row1 = [0, 1, -1] #0 refer to draw , 1 refer to you win , -1 refer to you lose
row2 = [-1, 0, 1] #columns are computer choices , rows are userr choices
row3 = [1, -1, 0]
mix = [row1, row2, row3]

if user_choice < 0 or user_choice > 2:
    print("Invalid number. Please enter a number between 0 and 2...")
else:
    print("Your choice:\n", images[user_choice])
    print("Computer Choice:", images[computer_choice])
    if mix[computer_choice][user_choice] == 0:
        print("It is a Draw!")
    elif mix[computer_choice][user_choice] == 1:
        print("You Win!")
    elif mix[computer_choice][user_choice] == -1:
        print("You Lose!")
