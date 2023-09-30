from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.iconbitmap(default='favicon.ico')
window.title("Pomodoro \U0001F47B ")
window.config(padx=100,pady=100)
# Canvas Widget
canvas=Canvas(width=200,height=224)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=tomato_img)
canvas.create_text(103,130,text=)
canvas.pack()

window.mainloop()