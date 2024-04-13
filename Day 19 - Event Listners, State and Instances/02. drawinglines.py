from turtle import Turtle, Screen

my_leo= Turtle()
my_screen = Screen()

def move_forward():
    my_leo.forward(10)
def move_backward():
    my_leo.backward(10)
def move_left():
    new_heading=my_leo.heading()+10
    my_leo.setheading(new_heading)
def move_right():
    new_heading=my_leo.heading()-10
    my_leo.setheading(new_heading)

def move_clear():
    my_leo.clear()
    my_leo.penup()
    my_leo.home()
    my_leo.pendown()

my_screen.listen()
#passing funciton into other function as a variable {Higher Order Function}
my_screen.onkey(key="f", fun=move_forward)
my_screen.onkey(key="b", fun=move_backward)
my_screen.onkey(key="r", fun=move_right)
my_screen.onkey(key="l", fun=move_left)
my_screen.onkey(key="c", fun=move_clear)

my_screen.exitonclick()