from turtle import *

def sqaure(s, size, width, color, x, y, edges):
    s.color(color)
    s.width(width)
    s.penup()
    s.goto(x, y)
    s.pendown()
    for i in range(edges):
        s.forward(size)
        s.left(360/edges*1)


s = Turtle()
s.speed(0)
sqaure(s, 100, 10, "yellow", 200, 200, 4)
sqaure(s, 150, 5, "brown", 150, 250, 4)
sqaure(s, 50, 2, "blue", 120, 120, 4)

done()
