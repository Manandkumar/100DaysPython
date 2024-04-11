from turtle import Turtle, Screen
import random

my_leo = Turtle()
my_screen =Screen()

colours = ["aquamarine","cyan","gray","coral","brown","green","firebrick"]

def draw_shapes(num_sides):
    angle =360/num_sides
    for _ in range(num_sides):
        my_leo.forward(100)
        my_leo.right(angle)

for shape_side in range (3,11):
    my_leo.color(random.choice(colours))
    draw_shapes(shape_side)

my_screen.onclick()