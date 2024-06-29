class DemoClass:
    a=12
    b=132
    c=45
    
    def sumvalue(self):
        print("sumvalue()_Addition_Result:-",20+30*30032)
        
DemoObject=DemoClass() #creation of a object
DemoObject_1=DemoClass() #creation of second a object
DemoObject.sumvalue();
print("this is an variable printed from DemoClass:-",DemoObject_1.a) #using an object to print a variable from a class
print("this is an variable printed from DemoClass:-",DemoObject.c) #     ""         ""        ""           ""
print("this is an variable printed from DemoClass:-",DemoObject_1.b) #     ""         ""        ""           ""

class DemoClass_2:
    a=10
DEmoobj=DemoClass_2() #creation of a object
print("this is an variable printed from DemoClass_2:-",DemoObject.a)