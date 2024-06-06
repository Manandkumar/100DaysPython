
from tkinter import *

window = Tk()
window.title ("Password Manager")


canvas = Canvas(width=200, height=200)
logo_img =PhotoImage(file="Day 29 - Password Manager\lock.png")
canvas.create_image(100,100,image=logo_img)
canvas.pack()




window.mainloop()