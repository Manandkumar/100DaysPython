from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width=600, height=400)

#components inside the window

#label 
mylabel= Label( text ="I'm a label ", font=("Arial", 24))
mylabel.pack(side="left")

# mylabel["text"] = "NEw Name -Anand"

#button 

def button_click():
    print("you pressed me ")


button = Button(text= "Press",command=button_click)
button.pack()















window.mainloop()
