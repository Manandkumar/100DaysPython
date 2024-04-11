from turtle import Turtle, Screen
my_leo = Turtle()
my_screen =Screen()
my_leo.shape("arrow")
my_leo.color("pink")

for _ in range(4):
    my_leo.forward(100)
    my_leo.right(90)

my_screen.exitonclick()