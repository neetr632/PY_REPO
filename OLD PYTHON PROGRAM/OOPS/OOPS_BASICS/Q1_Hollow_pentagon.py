from turtle import *
def pentagon(p,size,color,width,edges):
    p.color(color)
    p.width(width)
    for i in range(edges):
        p.forward(size)
        p.left(360/edges*1)
        
p =Turtle() 

pentagon(p,100, "red", 5, 5) 

pentagon(p,200, "black", 5, 5) 

pentagon(p,300, "orange", 5, 5) 

done()
