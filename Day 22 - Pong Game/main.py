from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("green")
screen.setup(width=800, height=600)
screen.title("Ping Pong - Anand")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("yellow")
paddle.shapesize(stretch_wid=5,stretch_len=1)
paddle.penup()
paddle.goto(350,0)

def go_up():
    if paddle.ycor()<240:
        new_y = paddle.ycor()+20
        paddle.goto(paddle.xcor(),new_y)

def go_down():
    if paddle.ycor()> -240:
        new_y = paddle.ycor()-20
        paddle.goto(paddle.xcor(),new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()