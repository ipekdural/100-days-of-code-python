height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:

    raise ValueError("Human Height should not be over 3 meters.")
    print("this will not be printed")
#The code block below raise will not execute
bmi = weight / height ** 2
print(bmi)


