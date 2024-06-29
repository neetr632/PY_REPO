# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
import math

class shapes:
    def __init__(self, radius, side, length, breadth):
        self.length = length
        self.breadth = breadth
        self.radius = radius
        self.side = side

    def square(self):
        area = self.side*self.side
        perimeter = 4*self.side
        return area, perimeter

    def rectangle(self):
        area = self.length * self.breadth
        perimeter = 2*(self.length+self.breadth)
        return area, perimeter

    def circle(self):
        area = math.pi * self.radius**2
        perimeter = 2 * math.pi * math.pi * self.radius
        return area, perimeter


side = int(input("enter the side value for the square: "))
length = int(input("enter the length value for the rectangle: "))
breadth = int(input("enter the breadth value for the rectangle: "))
radius = int(input("enter the radius value for the circle: "))

draw_s = shapes(side=side, length=length, breadth=breadth, radius=radius)
area, perimeter = draw_s.square()
print("area of the square: ", str(area) + " -|- " +
      "perimeter of the square : ", str(perimeter))
area, perimeter = draw_s.rectangle()
print("area of the rectangle: ", str(area) + " -|- " +
      "perimeter of the rectangle : ", str(perimeter))
area, perimeter = draw_s.circle()
print("area of the circle: ", str(area) + " -|- " +
      "perimeter of the circle: ", str(perimeter))
