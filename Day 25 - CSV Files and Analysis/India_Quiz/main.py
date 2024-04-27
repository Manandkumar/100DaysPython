import turtle
import pandas

screen =turtle.Screen()
screen.title ("INIDA STATES - QUIZ")
image= "./Day 25 - CSV Files and Analysis/India_Quiz/India_state.gif"
screen.addshape(image)
turtle.shape(image)
answer_state= screen.textinput(title="Guess the state",prompt= "State name:")

data = pandas.read_csv("./Day 25 - CSV Files and Analysis/India_Quiz/states.csv")
all_states = data.state.to_list()
guess_states =[]

while len(guess_states)<=30:
    answer_state =screen.textinput(title="Guess the state", prompt="Ampther state name?").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        # t.goto(state_data.x,state_data.y)
        t.goto(0,0)
       
        t.write(answer_state)



# def get_mouse_click(x,y):
#     print (x,y)

# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
