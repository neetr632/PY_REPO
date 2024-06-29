class DEMOclass:
    a = 10
    
    def __init__(self):
        print("this is a constructor,\nthat is executed by-itself")

    def sumvalue(self):
        print(self.a)
        self.c = self.a ** self.a
        print(self.c)
    
    def sumvalue_1(self,a,b):
        print(a+b, "is the value of the method/function --> sumvalue_1")

demoOBJECT = DEMOclass()
demoOBJECT.sumvalue()
demoOBJECT.sumvalue_1(23,12)