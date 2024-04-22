from turtle import Turtle

STARTING_POSITION = (0,-200)
MOVE_DISTANCE =10
FINISH_LINe_Y=280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    def go_up(self):
        self.forward(MOVE_DISTANCE)