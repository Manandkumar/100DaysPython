import turtle as t
import random
from turtle import Screen

my_leo = t.Turtle()
t.colormode(255)
my_screen = Screen()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour = (r,g,b)
    return colour

my_leo.speed(10)
my_leo.penup()
my_leo.setheading(225)
my_leo.forward(300)
my_leo.setheading(0)

number_of_dots =100
my_leo.hideturtle()


for dot_count in range(1,number_of_dots+1):
    my_leo.pendown()
    my_leo.dot(20,random_color())
    my_leo.penup()
    my_leo.forward(50)  
    if dot_count %10==0:
        my_leo.setheading(90)
        my_leo.forward(50)
        my_leo.setheading(180)
        my_leo.forward(500)
        my_leo.setheading(0)

my_screen.exitonclick()
