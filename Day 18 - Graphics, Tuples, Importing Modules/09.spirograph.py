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

my_leo.speed("fastest")
c_radius = int(input("Enter the radius of the circle: "))


for _ in range(200):
    my_leo.pencolor(random_color())
    my_leo.circle(c_radius)
    my_leo.setheading(my_leo.heading()+10)

my_screen.exitonclick()
