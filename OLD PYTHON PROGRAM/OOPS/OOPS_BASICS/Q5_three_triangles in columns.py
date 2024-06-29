from turtle import *

def column_trianlges(ct, size, color, width, x1, y1, edges):
    ct.color(color)
    ct.width(width)
    ct.penup()
    ct.goto(x1, y1)
    ct.pendown()

    for i in range(3):
        ct.forward(size)
        ct.left(360/edges)


ct1 = Turtle()
ct2 = Turtle()
ct3 = Turtle()
edges = 3

column_trianlges(ct1, 100, "green",3, -100, 100, edges)
column_trianlges(ct2, 100, "red",3, -100, 0, edges)
column_trianlges(ct3, 100, "blue",3, -100, -100, edges)

done()
