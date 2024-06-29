class Circle: 
    def __init__(self, radius):
        self.radius = radius #we prefer to initialize the attributes that we are sure to use further in the program!!
    def area(self):
        self.area = 3.14 * self.radius**2 
        print("the area is:",self.area)
        
    def perimeter(self):
        self.perimeter = 2 * 3.14 * self.radius
        print("the perimeter is:",self.perimeter)
        
radius = int(input("input your radius: ")) 
c1 = Circle(radius) #create a c1 object with the the value of user inputted radius
c1.area()
c1.perimeter()
 