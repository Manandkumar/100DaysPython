
from tkinter import *


#-------------- UI SETUP----------------------
window = Tk()
window.title ("Password Manager")
window.config(padx=40,pady=40)


canvas = Canvas(width=400, height=400)
logo_img =PhotoImage(file="Day 29 - Password Manager\lock.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)

#Labels 
website_label = Label(text="Website")
website_label.grid(row=1,column=0)
email_label=Label(text="Email / Username")
email_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)


window.mainloop()