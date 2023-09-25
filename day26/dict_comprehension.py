from random import randint

# Dict comprehension
# dict={key:value for item in list}
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {name: randint(1, 100) for name in names}

# Conditional Dict comprehension
# new_dict={new_key:new_value for (key,value) in dict.items if condition}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(student_scores)
print(passed_students)


#Dict to dict comprehension
#new_dict = {new_key: new_value for (key, value) in dict.items()}
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
weather_f={day:(temp*9/5)+32 for (day,temp) in weather_c.items()}

# Write your code 👇 below: (temp_c * 9/5) + 32 = temp_f



print(weather_f)
