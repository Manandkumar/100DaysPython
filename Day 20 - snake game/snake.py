from turtle import Turtle
SNAKE_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments =[]
        self.create_snake()
    def create_snake(self):
        for position in SNAKE_POSITIONS:
            snake_block= Turtle("square")
            snake_block.color("white")
            snake_block.penup()
            snake_block.goto(position)
            self.segments.append(snake_block)
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)


