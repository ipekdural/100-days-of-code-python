# Number Guessing Game
import random
import os


def compare(user_guess, actual_number):
    if user_guess > actual_number:
        print("Too high!")
    if user_guess < actual_number:
        print("Too low!")


def game(attempts):
    not_win = True
    while not_win:
        print(f"You have {attempts} attempts remaining to guess the number:")
        your_guess = int(input("  Make a guess: "))
        if your_guess == guessed_number:
            print(f"You got it! The answer was {your_guess} ")
            not_win = False

        else:
            compare(your_guess, guessed_number)
            attempts -= 1

            if attempts == 0:
                print(
                    f"You've run out of attempts. You Lose.\n   It was {guessed_number}"
                )
                not_win = False


play_again = True
while play_again:
    print(
        "Welcome to the Number Guessing Game!\nI'am thinking of a number between 1 and 100."
    )
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while game_level != "easy" and game_level != "hard":
        game_level = input("Invalid input. Type 'easy' or 'hard' :").lower()

    guessed_number = random.randint(1, 100)

    os.system("cls")
    if game_level == "easy":
        game(10)
    elif game_level == "hard":
        game(5)
    if (
        input(
            "Do you want to play another guessing game? Type 'y' for yes or any key to exit : "
        )
        != "y"
    ):
        play_again = False
    else:
        play_again = True
        os.system("cls")
print("Goodbye!")
#######################################################################################################
# Alternative
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
