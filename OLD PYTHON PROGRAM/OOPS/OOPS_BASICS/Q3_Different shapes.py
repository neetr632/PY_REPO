from turtle import *
import random


def three_shapes(ts, size, color, width, x, y, edges):
    ts.color(color)
    ts.width(width)
    ts.penup()  # lift the penup to write somewhere else
    ts.goto(x, y)
    ts.pendown()  # shift the pendown to write somewhere else
    for i in range(edges):
        ts.forward(size)
        ts.left(360/edges)


ts = Turtle()
shapes_num = int(input("Enter the number of shapes you want to generate: "))
if shapes_num >= 3:
    for i in range(shapes_num):
        random_value = random.randint(1, 100)
        x1 = random_value
        y1 = random_value
        col = ["red", "orange", "yellow", "green", "blue", "purple",
               "pink", "brown", "black", "white", "gray", "cyan", "magenta"]
        random_color = random.choice(col)
        random_edges = random.randint(3, 8)
        three_shapes(ts, 100, random_color, 5, x1, y1, random_edges)
elif shapes_num < 3:
    print("the number of shapes should be more than 3")
else:
    print("try again")
    
done()
# keep the window open until user closes