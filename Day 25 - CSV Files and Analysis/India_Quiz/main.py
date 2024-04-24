import turtle
screen =turtle.Screen()
screen.title ("INIDA STATES - QUIZ")
image= "./Day 25 - CSV Files and Analysis/India_Quiz/India_state.gif"
screen.addshape(image)

turtle.shape(image)

answer_state= screen.textinput(title="Guess the state",prompt= "State name:")

screen.exitonclick()

# def get_mouse_click(x,y):
#     print (x,y)

# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
