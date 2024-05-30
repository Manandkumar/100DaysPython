from tkinter import *

window = Tk()
window.title("My GIRD")
window.minsize(width=600, height=400)
window.config(padx=20,pady=20)


#components inside the window

#button funciton 
def button_click():
    mylabel= "Button Clicked"

#label 
mylabel= Label( text ="I'm a label ", font=("Arial", 12))
mylabel.grid(column=0,row=0)

# Button 
mybutton= Button(text="New Button", command=button_click)
mybutton.grid(column=2,row=0)
# Button 
mybutton2= Button(text="New Button2", command=button_click)
mybutton2.grid(column=1,row=1)

#Entry
myEntry = Entry(width=15)
myEntry.grid(column=3,row=2)


Label( text ="I'm a label ", font=("Arial", 12))
mylabel.grid(column=0,row=0)







window.mainloop()
