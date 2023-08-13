# Prime Number
def prime_checker(number):
    is_prime = True
    if number == 0 or number == 1:
        is_prime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)





#######################################################################################################

# CEASAR CİPHER
alphabet = [
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
]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
continue_ = True
# Check if the input direction is valid
while continue_:
    if direction != "encode" and direction != "decode":
        print("Invalid input. Please enter 'encode' or 'decode'.")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        text_list = []
        for i in text:
            text_list.append(i)

        def caesar(text, shift, direction):
            new_txt = ""
            if direction == "encode":
                for letter in text_list:
                    if letter not in alphabet:
                        j = text_list.index(letter)
                        new_txt += text_list[j]
                    else:
                        i = alphabet.index(letter)
                        new_txt += alphabet[(i + shift) % 26]

                print(f"The encoded text is {new_txt}")
            elif direction == "decode":
                for letter in text_list:
                    if letter not in alphabet:
                        j = text_list.index(letter)
                        new_txt += text_list[j]
                    else:
                        i = alphabet.index(letter)
                        new_txt += alphabet[(i - shift) % 26]
                print(f"The decoded text is {new_txt}")

        caesar(text, shift, direction)
    choice = input("Do you want to continue? Yes(y) or No(n).").lower()

    while choice != "y" and choice != "n":
        print("Invalid input. Please enter 'y' or 'n'.")
        choice = input("Do you want to continue? Yes(y) or No(n): ").lower()

    if choice == "y":
        continue_ = True
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
        ).lower()
    elif choice == "n":
        print("Good Bye!")
        continue_ = False
