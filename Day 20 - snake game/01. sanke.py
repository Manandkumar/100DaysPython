# part 1
from turtle import Turtle, Screen
import time

snake_screen = Screen()
snake_screen.setup(width=500,height=500)
snake_screen.bgcolor("black")
snake_screen.title("My Snake Game!")
snake_screen.tracer(0)

# Crate a snake body [using 3 block]

snake_position = [(0,0),(-20,0),(-40,0)]
segments =[]
for position in snake_position:
    snake_block= Turtle("square")
    snake_block.color("white")
    snake_block.penup()
    snake_block.goto(position)
    segments.append(snake_block)
    

# Move the snake 

game_on = True

while game_on:
    snake_screen.update()
    time.sleep(1)
    for seg in segments:
        seg.forward(20)
        

def move_forward():
    snake_block.forward(10)
def move_backward():
    snake_block.backward(10)
def move_left():
    new_heading=snake_block.heading()+10
    snake_block.setheading(new_heading)
def move_right():
    new_heading=snake_block.heading()-10
    snake_block.setheading(new_heading)


# Control the snale using keyboard controls

# Part 2

# Detect collission with food 

# Dreate the scoreboard

# Detect the collision with wall

# Detect the collision with tail

snake_screen.exitonclick()