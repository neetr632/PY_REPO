class A:
    def displayA(self):
        print("welcome to Wscubetech A")
        
class B(A):
    def displayB(self):
        print("welcome to WSCUBETECH B")

class C(B):
    def displayC(self):
        print("welcome to WSCUBETECH C")
        


obg_1 = B()
obg_1.displayA()

obg = C()
obg.displayB()
