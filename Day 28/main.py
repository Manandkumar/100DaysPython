from tkinter import *

black = "#1d3c45"
orange = "#d2601a"
cream = "#fff1e1"
p_number =25


# Timer Reset



#Timer Mechanism

def start_timer():
    count_down(5 *60)

# Countdown 

def count_down(count):


    canvas.itemconfig(timer_text,text=count)
    if count > 0:
        window.after(1000,count_down, count-1)


# UI Setup 

window = Tk()
window.title ("Pamodoro")
window.config(padx=10,pady=10, bg=black)



title_label = Label(text= "Timer",fg=orange,bg=black,font=("Arial",50))
title_label.grid(column=1,row=0)


canvas = Canvas(width=300, height=300,bg=cream)
timer_text=canvas.create_text(150,150, text="00:00", fill="red",font=("Arial",18))
canvas.grid(column=1,row=1)



start_button = Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2,row=2)

check_mark = Label(text="✔",fg=orange,bg=black)
check_mark.grid(column=1,row=3)














window.mainloop()