from turtle import Turtle, Screen

my_leo= Turtle()
my_screen = Screen()

def move_forward():
    my_leo.forward(10)

my_screen.listen()
#passing funciton into other function as a variable {Higher Order Function}
my_screen.onkey(key="space", fun=move_forward)
my_screen.exitonclick()