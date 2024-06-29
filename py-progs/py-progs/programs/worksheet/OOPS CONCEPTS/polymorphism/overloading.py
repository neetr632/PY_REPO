class AREA:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print("area of the rectangle:",(a*b))
        elif a!=None:
            print("the area of the square:",(a*a))
        else:
            print("nothing to find as no aruguements were passed")
            
obj1=AREA()
obj1.find_area()
obj1.find_area(10)
obj1.find_area(10,20)