from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width=600, height=400)

mylabel= Label( text ="I'm a label ", font=("Arial", 24))
mylabel.pack(side="left")