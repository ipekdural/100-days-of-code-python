# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
#
import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# new_dict={new_key:new_value for (index, row) in dataframe.iterrows()}  converting a data frame to a dictionary


data = pandas.read_csv("nato_phonetic_alphabet.csv")  # creating dataframe from csv file
new_data_dict = {row.letter: row.code for (index, row) in data.iterrows()}  # converting a data frame to a dict
# print(new_data_dict)
#
# dict={key:value for item in list}
while True:
    user_answer=input("Enter a word: ").upper()
    try:
        coded_word=[new_data_dict[letter] for letter in user_answer if letter!=' ']

    except KeyError:
        print("Please enter a string.")
    else:

        print(coded_word)
        break
