from tkinter import *
window= Tk()
window.title("Mile To Kilometers")
window.minsize(width=300,height=200)
window["padx"]=80
window["pady"]=50
def button_clicked():
    label_result["text"]=f"{int(input.get())*1.60934} km"
label_miles=Label(text="Miles:", font=("Ariel", 12, "italic"))
label_miles.grid(column=0, row=0)
input=Entry(width=10)
input.grid(column=1,row=0)
x=20
label_km=Label(text=f"Km:", font=("Ariel", 12, "italic"),anchor="e")
label_km.grid(column=0, row=1)
label_result=Label(font=("Ariel", 12, "italic"),anchor="e")
label_result.grid(column=1, row=1)
button= Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=3)
window.mainloop()