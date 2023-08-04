#Type Conversion
num_char =len(input("What is your name?"))
new_num_char=str(num_char)#converting integer to string format
print("Your name has "+new_num_char+" characters.")



#input function always creates a string data type . So we have to convert output of input.
age = input("What is your current age? ")
new_age=int(age)#converting string to int
day=(90-new_age)*365
week=(90-new_age)*52
month=(90-new_age)*12
print(f"You have {day} days, {week} weeks, and {month} months left.")




#f-Strings
score=0
height=1.8
isWinning=True
print(f"score is {score}  and height is {height} and ur winning is {isWinning}.")



#Tip Calculator
print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill? $"))
tip_percentage=int(input("What percentage tip would you like to give? 10,12 or 15 ?"))
people_num=int(input("How many people to split the bill? "))
bill= round((total_bill+((total_bill*tip_percentage)/100))/people_num,2)

print(f"Each person shoul pay ${bill}")