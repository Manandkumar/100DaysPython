import time 
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manger = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up,"Up")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

    car_manger.create_car()
    car_manger.move_car()

    #detect collision 
    for car in car_manger.all_car:
        if car.distance(player) <20:
            game_on= False
            scoreboard.GameOver()
    #detect the crossing 
    if player.is_at_finish_line():
        player.go_to_start()
        car_manger.level_up()
        scoreboard.increase_level()

    

screen.exitonclick()