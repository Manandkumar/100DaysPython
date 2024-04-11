# Draw Square, Pentagon, hexagon, heptagon, octagon, nonagoan and decagon
from turtle import Turtle, Screen
my_leo = Turtle()
my_screen =Screen()
my_leo.shape("arrow")
my_leo.color("pink")
#square
for _ in range(4):
    my_leo.forward(100)
    my_leo.right(90)
#pentagon
my_leo.color("green")
for _ in range(5):
    my_leo.forward(100)
    my_leo.right(72)

#Hexagon
my_leo.color("orange")
for _ in range(6):
    my_leo.forward(100)
    my_leo.right(60)

#Heptagon
my_leo.color("black")
for _ in range(7):
    my_leo.forward(100)
    my_leo.right(51.43)

#octagon
my_leo.color("red")
for _ in range(8):
    my_leo.forward(100)
    my_leo.right(45)

# Nonagoan and decagon
my_leo.color("cyan")
for _ in range(9):
    my_leo.forward(100)
    my_leo.right(40)

# Decagon
my_leo.color("olive")
for _ in range(10):
    my_leo.forward(100)
    my_leo.right(36)

my_screen.exitonclick()