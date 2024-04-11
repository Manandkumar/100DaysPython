from turtle import Turtle, Screen

my_leo = Turtle()
my_screen= Screen()

my_leo.shape("arrow")
my_leo.color("blue")

for _ in range(25):
    my_leo.pendown()
    my_leo.forward(5)
    my_leo.penup()
    my_leo.forward(5)

my_screen.exitonclick()

