from turtle import Turtle, Screen
import random
my_screen =Screen()

def move_forward():
    leo_1.forward(random.randint(10))

#setting up the screen size
my_screen.setup(800,600)
user_color= my_screen.textinput(title= "Make your bet!", prompt= "Which colour turtle you wanna bet on: ")
colours = ["blue","green","orange","red","yellow","purple"]
y_axis = [-70,-40,-10,20,50,80]
for index in range (0,5):
    leo_1 =Turtle(shape="turtle")
    leo_1.penup()
    leo_1.color(colours[index])
    leo_1.goto(x=-380,y=y_axis[index])
    leo_1.forward(random.randint(1,10))


#state = differences between each object 


my_screen.exitonclick()