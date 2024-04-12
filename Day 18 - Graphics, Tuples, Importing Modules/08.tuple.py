from turtle import Turtle, Screen
import random

my_leo= Turtle()
my_screen =Screen()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

direction = [0,90,180,270]
my_leo.width(10)
my_leo.speed(10)

for _ in range (250):
    my_leo.color(120)
    my_leo.forward(30)
    my_leo.setheading(random.choice(direction))

my_screen.exitonclick()