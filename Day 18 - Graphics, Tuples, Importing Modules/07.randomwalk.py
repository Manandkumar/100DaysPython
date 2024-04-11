from turtle import Turtle, Screen
import random

my_leo = Turtle()
my_screen =Screen()

colours = ["aquamarine","cyan","gray","coral","brown","green","firebrick"]
direction = [0,90,180,270]
my_leo.width(10)
my_leo.speed(10)

for _ in range (250):
    my_leo.color(random.choice(colours))
    my_leo.forward(30)
    my_leo.setheading(random.choice(direction))

my_screen.onclick()