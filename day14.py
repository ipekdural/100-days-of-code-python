# Higher Lower Game
from game_data_day14 import data
from random import choice
import os

logo = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

"""


def get_random_account():
    return choice(data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name} , a/an {description} , from {country}"


def check_answer(a, b, guess):
    if a > b:
        return guess == "a"
    else:
        return guess == "b"


def game():
    restart = True
    while restart:
        score = 0
        game_should_continue = True
        account_a = get_random_account()
        account_b = get_random_account()
        while game_should_continue:
            account_a = account_b
            account_b = get_random_account()
            while account_a == account_b:
                account_b = get_random_account
            print(f"Compare A: {format_data(account_a)}.")
            print(logo)
            print(f"Against B: {format_data(account_b)}.")
            guess = input("Who has more follower? Type 'A' or 'B'.").lower()
            a_follower = account_a["follower_count"]
            b_follower = account_b["follower_count"]
            os.system("cls")
            if check_answer(a_follower, b_follower, guess):
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                game_should_continue = False
        if (
            input("Do you want to play again? Type 'y' to yes , Press any key to exit.")
            != "y"
        ):
            restart = False
        else:
            game()


game()
