# Its possible to import EVERYTHING from a module via the *, this is kinda bad practice
# E.G. from turtle import *

# You can give a module an alias using "as" which is a little like re-naming it
# E.G.
# from turtle as t
# tim = t.Turtle()

from turtle import Turtle, Screen
import random as r

tim = Turtle()
tim.shape("turtle")
tim.shapesize(2)
tim.color("purple")
tim.pensize(3)

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
