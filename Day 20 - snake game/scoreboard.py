from turtle import Turtle
ALIGNMENT = "center"
FONT =("Courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        self.penup()
        self.color=("white")
        self.goto(0,0)
        self.write(f"Score: {self.score}", align=ALIGNMENT,font=FONT)
        self.hideturtle()
    
    def increase_score(self):
        self.score+=1
        self.write(f"Score: {self.score}", align=ALIGNMENT,font=FONT)
        print(self.score)
