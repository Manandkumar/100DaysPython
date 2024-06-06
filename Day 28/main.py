from tkinter import *
import math

BLACK = "#1d3c45"
ORANGE = "#d2601a"
CREAM = "#fff1e1"
p_number =25
reps =0

WORK_MIN = 5
SHORT_BREAK_MIN=5
LONG_BREAK_MIN=20

# Timer Reset



#Timer Mechanism

def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60

    #if it's the 1/3/5/7 rep:
    count_down(work_sec)
    if reps %8 ==0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=ORANGE)
    elif reps %2 ==0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=CREAM)
    else:
        count_down(work_sec)
        title_label.config(text="Break", fg=BLACK)


# Countdown 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec <10:
        count_sec= f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min} : {count_sec}")
    if count > 0:
        window.after(1000,count_down, count-1)
    else:
        start_timer()
        marks=""
        work_session= math.floor(reps/2)
        for _ in range(work_session):
            marks+="✔"
        check_mark.config(text=marks)


# UI Setup 

window = Tk()
window.title ("Pamodoro")
window.config(padx=10,pady=10, bg=BLACK)



title_label = Label(text= "Timer",fg=ORANGE,bg=BLACK,font=("Arial",50))
title_label.grid(column=1,row=0)


canvas = Canvas(width=300, height=300,bg=CREAM)
timer_text=canvas.create_text(150,150, text="00:00", fill="red",font=("Arial",18))
canvas.grid(column=1,row=1)



start_button = Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2,row=2)

check_mark = Label(fg=ORANGE,bg=BLACK)
check_mark.grid(column=1,row=3)














window.mainloop()