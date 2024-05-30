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
canvas = Canvas(width=500, height=500,bg=cream)
canvas.create_text(250,250, text="00:00", fill="red",font=("Arial",18))


canvas.pack()












window.mainloop()