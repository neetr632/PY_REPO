from turtle import *
t1 = Turtle()  # t1 is the object here of class turtle
t1.color("orange")
t1.width(5)

t1.begin_fill()
for i in range(5):
    t1.forward(200)
    t1.left(144)
t1.end_fill()
done()
