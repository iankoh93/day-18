# It's possible to import EVERYTHING from a module via the *, this is kinda bad practice
# E.G. from turtle import *

# You can give a module an alias using "as" which is a little like re-naming it
# E.G.
# from turtle as t
# tim = t.Turtle()

from turtle import Turtle, Screen
import turtle as t
import random as r

# color = ["red", "green", "blue", "yellow", "pink", "purple", "aquamarine", "gold", "turquoise", "cyan", "lavender", "snow3", "grey", "violet"]

color = (1, 3, 8)
direction = [0, 180, 270, 90]
t.colormode(255)


def choose_direction():
    angle = r.choice(direction)
    tim.right(angle)


def walk_random_distance():
    length = r.randint(10, 50)
    tim.forward(length)


def change_color():
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    new_color = (red, green, blue)
    tim.color(new_color)


tim = Turtle()
tim.shape("arrow")
tim.shapesize(1)
tim.color("black")
tim.pensize(2)
tim.speed(100)

number_of_turns = 75

for _ in range(number_of_turns):
    change_color()
    tim.circle(100)
    tim.right(360/number_of_turns)


# for _ in range(200):
#     change_color()
#     choose_direction()
#     walk_random_distance()

# tim.penup()
# tim.left(90)
# tim.forward(500)
# tim.left(90)
# tim.forward(100)
# tim.right(180)
# tim.pendown()
#
# for i in range(3, 30):
#     for _ in range(1, i+1):
#         tim.forward(100)
#         tim.right(360/i)


screen = Screen()
screen.exitonclick()
