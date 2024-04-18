from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        self.color=("red")
        self.write(f"Score: {self.score}", align="center",font=("Arial",24, "normal"))
        self.hideturtle()
        self.goto(0,250)