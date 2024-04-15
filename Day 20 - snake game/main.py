# part 1
from turtle import Turtle, Screen
from snake import Snake
import time

snake_screen = Screen()
snake_screen.setup(width=500,height=500)
snake_screen.bgcolor("black")
snake_screen.title("My Snake Game!")
snake_screen.tracer(0)

snake = Snake()
# Move the snake 

game_on = True

while game_on:
    snake_screen.update()
    time.sleep(0.1)
    snake.move()
    
# Control the snale using keyboard controls

# Part 2

# Detect collission with food 

# Dreate the scoreboard

# Detect the collision with wall

# Detect the collision with tail

snake_screen.exitonclick()