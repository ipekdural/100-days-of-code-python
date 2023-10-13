import tkinter.messagebox
import pyperclip
from time import sleep
from random import *
from tkinter import*
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
chars=["!", "#", "%", "&", "(", ")", "*", "+"]
nums=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
low_letters=[    "a",
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
    "z"]
capitalize_letter=[
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z"]



def generate_button_clicked():
    password_entry.delete(0,END)
    char_num = randint(4, 4)
    num_num = randint(2, 4)
    c_letter_num = randint(2, 4)
    rand_chars = sample(chars, char_num)
    rand_nums = sample(nums, num_num)
    rand_letters_c = sample(capitalize_letter, c_letter_num)
    rand_letters_l = sample(low_letters, 16 - char_num - num_num - c_letter_num)
    password = rand_chars + rand_nums + rand_letters_c + rand_letters_l
    password_shuffled = sample(password, 16)
    password_string = "".join(password_shuffled)

    password_entry.insert(0,password_string)
    pyperclip.copy(password_string)


#*********ALTERNATIVE**********
    # password_letters = [choice(letters) for _ in range(randint(8, 10))]
    # password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    # password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    #
    # password_list = password_letters + password_symbols + password_numbers
    # shuffle(password_list)
    #
    # password = "".join(password_list)
    # password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
#file process
def add_button_clicked():
    web_entry=website_entry.get()
    mail_entry=email_entry.get()
    pass_entry=password_entry.get()
    if web_entry=="" or mail_entry=="" or pass_entry=="":
        tkinter.messagebox.showwarning("Error","Please fill the all blanks!")
    else:
        question=tkinter.messagebox.askyesno("Question","Are you sure?",default="yes")
        if question==YES:
            with open("data.txt","a") as file:
                file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            sleep(0.5)
            tkinter.messagebox.showinfo("Information","Your password has been saved successfully.")
            password_entry.delete(0,END)
            website_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager🔑")
window.config(padx=20,pady=20)
window.iconbitmap(default='favicon.ico')
canvas=Canvas(height=200,width=200)
image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(column=1,row=0)


website_label=Label(text="Website:")
website_label.grid(column=0,row=1)
email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

placeholder="example@gmail.com"
website_entry=Entry(width=50)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=50)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,placeholder)
password_entry=Entry(width=32)
password_entry.grid(column=1,row=3)

generate_button=Button(text="Generate Password",width=14,command=generate_button_clicked)
generate_button.grid(column=2,row=3)
add_button=Button(text="Add",width=30,command=add_button_clicked)
add_button.grid(column=1,row=4,columnspan=2)





window.mainloop()
