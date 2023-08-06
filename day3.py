# if-elif-else
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / height**2)
if bmi < 18.5:
    print("Your BMI is {0:d}, you are underweight.".format(bmi))
elif bmi < 25:
    print("Your BMI is {0:d}, you have a normal weight.".format(bmi))
elif bmi < 30:
    print("Your BMI is {0:d}, you are slightly overweight.".format(bmi))
elif bmi < 35:
    print("Your BMI is {0:d}, you are obese.".format(bmi))
else:
    print("Your BMI is {0:d}, you are clinically obese.".format(bmi))


# Leap Year Calculator
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


# Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1 = name1.lower()
name2 = name2.lower()
t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")
total1 = t + r + u + e
l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e2 = name1.count("e") + name2.count("e")
total2 = l + o + v + e2
score = str(total1) + str(total2)
int_score = int(score)
if int_score < 10 or int_score > 90:
    print(f"Your score is {int_score}, you go together like coke and mentos.")
elif int_score < 50 and int_score > 40:
    print(f"Your score is {int_score}, you are alright together.")
else:
    print(f"Your score is {int_score}.")


# Treasure Island
print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("There are two roads ahead. Choose one. Right(R) or Left(l)?  ").lower()

if choice1 == "l":
    choice2 = input("You\'ve come to a lake. There is an island in the middle of the lake.You can wait for a boat or you can swim to island.  Swim(S) Or Wait(W)?").lower()
    if choice2 == "w":
        choice3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? Red(R),Yellow(Y) or Blue(B)?").lower()
        if choice3 == "r":
            print("Opss...You burned by fire!🔥")
        elif choice3 == "b":
            print("Opss...You eaten by monster beasts.👹")
        elif choice3 == "y":
            print("You found the treasure! You Win!🥇")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("Oh NO! You attacked by piranhas.🐠")
else:
    print("Opss...You are trapped by cannibals.💀")
