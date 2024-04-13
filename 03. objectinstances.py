from turtle import Turtle, Screen
import random
my_screen =Screen()

race_on =False

def move_forward():
    leo.forward(random.randint(10))

#setting up the screen size
my_screen.setup(800,600)
user_color= my_screen.textinput(title= "Make your bet!", prompt= "Which colour turtle you wanna bet on: ")
colours = ["blue","green","orange","red","yellow","purple"]
y_axis = [-70,-40,-10,20,50,80]
all_turles=[]

for index in range (0,5):
    leo =Turtle(shape="turtle")
    leo.penup()
    leo.color(colours[index])
    leo.goto(x=-380,y=y_axis[index])
    all_turles.append(leo)

#state = differences between each object 
if user_color:
    race_on= True
while race_on:
    for turtle in all_turles:
        move_forward = random.randint(0,10)
        turtle.forward(move_forward)


my_screen.exitonclick()