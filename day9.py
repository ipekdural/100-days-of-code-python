##Python Dictionaries

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary.
print(programming_dictionary["Function"])

# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#######################################

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
}

# Nesting Dictionaries in Lists

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]


#############################################################
# Secret Auction

import os


def max_bid(name, bid):
    max_bid_ = max(values)
    for i in dict_auction:
        if max_bid_ == dict_auction[i]:
            max_bid_key = i
    print(f"The winner is {max_bid_key} with a bid of ${max_bid_}.")


values = []
dict_auction = {}
_continue = True
print("Welcome to the secret auction program.")
while _continue:
    name = input("What is your name? : ")
    bid = int(input("What is your bid? $:"))
    choice = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    dict_auction[name] = bid
    for key in dict_auction:
        values.append(dict_auction[key])
    while choice != "yes" and choice != "no":
        choice = input("Invalid input. Please type 'yes' or 'no' :")
    if choice == "yes":
        _continue = True
        os.system("cls")

    elif choice == "no":
        max_bid(name, bid)
        _continue = False


#############################################################################
# Alternative Secret Auction
bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system("cls")
