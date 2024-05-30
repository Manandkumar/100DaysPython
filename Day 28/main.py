from tkinter import *

black = "#1d3c45"
orange = "#d2601a"
cream = "#fff1e1"



# Timer Reset

#Timer Mchanism

# Countdown 

# UI Setup 

window = Tk()
window.title ("Pamodoro")
window.config(padx=10,pady=10, bg=black)

title_label = Label(text= "Timer",fg=orange,bg=black,font=("Arial",50))


canvas = Canvas(width=300, height=300,bg=cream)
canvas.create_text(150,150, text="00:00", fill="red",font=("Arial",18))


canvas.pack()












window.mainloop()