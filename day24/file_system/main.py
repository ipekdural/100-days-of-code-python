# file=open("my_file.txt")
# contents= file.read()
# print(contents)#print the contents of file to console
# file.close()

# with open("my_file.txt") as file:#this way you dont have to close file
#     contents= file.read()
#     print(contents)#print the contents of file to console

# with open("my_file.txt",mode="w") as file:#open method is read-only by default we have to change the mode to write
#     file.write("new text!")#this way old text has been deleted and 'new text!' has been written

# with open("my_file.txt",mode="a") as file:
#     file.write("new text appended !")#this method append the writen text to old text

with open("new_file.txt", mode="a") as file:#creating new text file and add the written content. This only works in 'w' mode
    file.write("new text file created !")

