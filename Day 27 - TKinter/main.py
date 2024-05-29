from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width=600, height=400)

#components inside the window

#label 
mylabel= Label( text ="I'm a label ", font=("Arial", 24))
mylabel.config(text="New Text")
mylabel.grid(column=0,row=0)

# mylabel.pack(side="left")

# mylabel["text"] = "NEw Name -Anand"

#button 

def button_click():
    mylabel["text"]= "Button is clicked"
    mylabel.config(text="Button is clicked!")
    entry_text=input.get()
    mylabel.config(text=entry_text)
    print("you pressed me ")


button = Button(text= "Press",command=button_click)
button.pack()

#entry

input = Entry(width=10)
input.pack()















window.mainloop()
