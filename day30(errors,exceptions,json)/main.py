#FileNotFound
try:
    file =open("a_file.txt")#if there is no such file it will go to exception block
    a_Dict={"key":"value"}
    print(a_Dict["key "])
except FileNotFoundError:
    file=open("a_file.txt","w")#do this if something wrong in try block
except KeyError as error_message:
    print(f"The key {error_message} does not exist!")
else:
    #if there is an exception else block will not execute
    # if there are no exceptions this code block will execute
    content=file.read()
    print(content)
finally:
    #no matter what this code block will execute
    file.close()
    print("File has closed")
