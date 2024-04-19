# part 1
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


snake_screen = Screen()
snake_screen.setup(width=500,height=500)
snake_screen.bgcolor("black")
snake_screen.title("My Snake Game!")
snake_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard=Scoreboard()

# Move the snake 
snake_screen.listen()
snake_screen.onkey(snake.up, "Up")
snake_screen.onkey(snake.down, "Down")
snake_screen.onkey(snake.left, "Left")
snake_screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    snake_screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)< 15:
        food.refresh()
        scoreboard.increase_score()
# Detect the collision with wall
    if snake.head.xcor()> 280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor()< -280:
        game_on= False
        scoreboard.game_over()
# Detect the collision with tail

snake_screen.exitonclick()