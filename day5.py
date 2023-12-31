# High Score

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

the_highest_score = student_scores[0]
for score in range(1, len(student_scores)):
    if the_highest_score < student_scores[score]:
        the_highest_score = student_scores[score]
print("The highest score in the class is: ", the_highest_score)


# Range Function
#    for number in range(x,y,z): -----> range is between x and y (y is not included), and it increases by z
#         print(number)


# ************************************************************************************************

# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
pass_letters = []
pass_symbols = []
pass_nums = []
for i in range(0, nr_letters):
    random_letter = random.choice(letters)
    pass_letters.append(random_letter)

for i in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    pass_symbols.append(random_symbol)


for i in range(0, nr_numbers):
    random_num = random.choice(numbers)
    pass_nums.append(random_num)


password = pass_letters + pass_symbols + pass_nums
random.shuffle(password)
password_str = ""
for eleman in password:
    password_str += eleman
print(password_str)

# *************************************************************************************************

# Alternative Password Generator
rand_letters = random.sample(letters, nr_letters)
rand_numbers = random.sample(numbers, nr_numbers)
rand_symbols = random.sample(symbols, nr_symbols)
password = rand_letters + rand_numbers + rand_symbols

length = len(password)

randomized_password = random.sample(password, length)
string = "".join(randomized_password)

print(string)
