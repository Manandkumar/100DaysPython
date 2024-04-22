import time 
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manger = CarManager()
screen.listen()
screen.onkey(player.go_up,"Up")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()