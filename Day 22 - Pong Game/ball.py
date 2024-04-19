from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape("circle")
        self.color("yellow")
        self.penup()
    
    def move(self):
        if self.xcor() <375 and self.ycor< -370:
            new_x = self.xcor()+1
            new_y = self.ycor()+1
            self.goto(new_x,new_y)
