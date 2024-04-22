import time 
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()