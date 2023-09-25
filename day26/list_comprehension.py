# # LIST COMPREHENSION
# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]  # [new_item for item in list]
# print(new_numbers)
#
# # we can use it for strings too
# name = "Ipek"
# letter_list = [letter for letter in name]  # do nothing to item just adding to list
# print(letter_list)
#
# # using it with range func
# range_list = [n * 2 for n in range(1, 5)]
# print(range_list)

# CONDITIONAL LIST COMPREHENSION
num_list=[1,2,3,4,5,6,7]
small_num_list=[num for num in num_list if num<5]
print(small_num_list)
name_list=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
upper_case_long_names=[name.upper() for name in name_list if len(name)>5]
print(upper_case_long_names)



