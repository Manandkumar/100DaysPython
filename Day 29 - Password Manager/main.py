
from tkinter import *

window = Tk()
window.title ("Password Manager")
window.config(padx=40,pady=40)


canvas = Canvas(width=400, height=400)
logo_img =PhotoImage(file="Day 29 - Password Manager\lock.png")
canvas.create_image(100,100,image=logo_img)
canvas.pack()




window.mainloop()