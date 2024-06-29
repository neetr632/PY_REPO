class Method_cons:
    def __init__(self, a): #called by_itself when the code runs.
        self.a = a

    def showValue(self):
        print(self.a*self.a)
        
    def wscubetech(self):
        print("Welcome To Wscubetech")


obj = Method_cons(10)
obj.showValue()
obj.wscubetech()
