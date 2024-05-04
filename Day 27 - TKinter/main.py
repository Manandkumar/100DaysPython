import tkinter
window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=600, height=400)

#components inside the window

#label 
mylabel= tkinter.Label( text ="I'm a label ", font=("Arial", 24))
mylabel.pack(side="left")













window.mainloop()
