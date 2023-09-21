#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as names:
    for name in names:
        new_name=name.strip()
        with open("Input/Letters/starting_letter.txt",mode='r') as text:
            letter=text.read()
            new_letter=letter.replace("[name]",new_name)
            print(new_letter)
            path=f"Output/ReadyToSend/{new_name}.txt"
            with open(path,mode="w") as send:
                send.write(new_letter)



