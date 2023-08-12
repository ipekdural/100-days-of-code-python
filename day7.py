import random
import os


word_list = [
    "Apple",
    "Banana",
    "Cherry",
    "Orange",
    "Lemon",
    "Grape",
    "Watermelon",
    "Strawberry",
    "Blueberry",
    "Raspberry",
    "Pineapple",
    "Apricot",
    "Mango",
    "Kiwi",
    "Papaya",
    "Peach",
    "Coconut",
    "Plum",
    "Pear",
    "Dog",
    "Cat",
    "Elephant",
    "Lion",
    "Tiger",
    "Giraffe",
    "Kangaroo",
    "Penguin",
    "Koala",
    "Zebra",
    "Canada",
    "Mexico",
    "Brazil",
    "Australia",
    "China",
    "India",
    "Japan",
    "France",
    "Germany",
    "Table",
    "Chair",
    "Lamp",
    "Couch",
    "Desk",
    "Bookshelf",
    "Computer",
    "Mirror",
    "Painting",
    "Window",
    "Clock",
    "Plant",
    "Vase",
    "Piano",
    "Guitar",
    "Microwave",
    "Refrigerator",
    "Umbrella",
    "Backpack",
    "Shoe",
    "Socks",
    "Hat",
    "Gloves",
    "Belt",
    "Watch",
    "Scissors",
    "Notebook",
    "Pen",
    "Pencil",
    "Sunny",
    "Cloudy",
    "Rainy",
    "Windy",
    "Snowy",
    "Thunderstorm",
    "Foggy",
    "Hail",
    "Rainbow",
    "Tornado",
]
stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========================================================================
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========================================================================
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========================================================================
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========================================================================""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========================================================================
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========================================================================
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========================================================================
""",
]
logo = """ 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    """
print(logo)

chosen_word = random.choice(word_list).upper()
print(chosen_word)
word_lenght = len(chosen_word)
lives = 6
display = []
for i in range(word_lenght):
    display += "_"
end_of_game = False
guessed_letters = []
while not end_of_game:
    guess = input("Guess a letter: ").upper()
    os.system("cls")
    print(logo)
    if guess in guessed_letters:
        print(f"You have already guessed {guess}.")
        print(f"{' '.join(display)}")
        if "_" not in display:
            end_of_game = True
            print("You win!")
        print(stages[lives])
    else:
        guessed_letters.append(guess)

        for i in range(word_lenght):
            letter = chosen_word[i]

            if letter == guess:
                display[i] = guess

        if guess not in display:
            lives = lives - 1
            if lives == 0:
                print(f"You lose. The word you couldn't cope with was {chosen_word}.")
                end_of_game = True
            else:
                print(f"You guessed {guess},that's not in the word.You lose a life.")
        print(f"{' '.join(display)}")
        if "_" not in display:
            end_of_game = True
            print("You win!")
        print(stages[lives])
