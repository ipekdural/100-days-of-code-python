# Functions with Outputs
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    f"Result: {formated_f_name} {formated_l_name}"


# Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
# or printing output directly
print(
    format_name(input("What is your first name? "), input("What is your last name? "))
)

# Already used functions with outputs.
length = len(formatted_name)


# Return as an early exit
def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


################################################################################################
# Calculator
import os
import sys

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    """returns to addition of n1 and n2"""
    return n1 + n2


def sub(n1, n2):
    """returns to subtraction of n1 and n2"""
    return n1 - n2


def mul(n1, n2):
    """returns to multiplication of n1 and n2"""
    return n1 * n2


def div(n1, n2):
    """returns to division of n1 and n2"""
    return n1 / n2


operations = {"+": add, "-": sub, "*": mul, "/": div}

opr_list = []

should_continue = True


def calculator():
    print(logo)
    num1 = float(input("What's first number? :"))
    for operators in operations:
        print(operators)
        opr_list.append(operators)

    while should_continue:
        operation_symbol = input("Pick an operator : ")
        while operation_symbol not in opr_list:
            operation_symbol = input(
                "Invalid operation. Please enter a valid operation."
            )
        num2 = float(input("What's next number? :"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(
            f"Type 'y' to continue calculating with {answer} or type 'n' to restart calculator.\nPress 'x' to exit."
        ).lower()
        while choice != "y" and choice != "n" and choice != "x":
            choice = input("Invalid input. Please type 'y' , 'n' or 'x' :")
        if choice == "y":
            num1 = answer

        elif choice == "n":
            os.system("cls")
            calculator()
        elif choice == "x":
            print("Good Bye!")
            sys.exit()


calculator()
