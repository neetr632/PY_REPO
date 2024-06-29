from turtle import *
import random


def ten_circles(tes, color, width, x, y, no_of_circle, radius):
    tes.color(color)
    tes.width(width)

    for i in range(no_of_circle):
        x1 = random.randint(1, 300)
        y1 = random.randint(1, 300)
        tes.penup()
        tes.goto(x1, y1)
        tes.pendown()
        tes.circle(radius)


tes = Turtle()

nos_of_circle = int(input("enter the desired value:"))
if nos_of_circle > 0:
    ten_circles(tes, "red", 3, 0, 0, nos_of_circle, 50)
else:
    print("please enter a positive integer")
done()
