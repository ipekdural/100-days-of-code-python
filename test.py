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
