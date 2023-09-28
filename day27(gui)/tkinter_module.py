from tkinter import *

window = Tk()
window.title("GUI program")
window.minsize(width=500, height=500)

# Create a LABEL
my_label = Label(text="This is a label", font=("Ariel", 24, "italic"), bg="red")
my_label.pack(side="top", fill="none", expand=False, anchor="w", padx=30, pady=30, ipady=30,
              ipadx=30)  # with this method my_label will apeear on screen

# Changing properties of components
# my_label["text"]="New text"
my_label.config(text="New text")



# Create an ENTRY
input= Entry(width=30)
input.pack()

# Create A BUTTON
def button_clicked():
    my_label["text"]=input.get()


my_button = Button(text="Button",font=("Ariel",12,"bold"),command=button_clicked) # anchor align text in button
my_button.pack()

# Unlimited Arguments
def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)


add(1, 2, 3)

window.mainloop()
