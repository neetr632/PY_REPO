# Write a Python program to create a calculator class. Include methods for basic arithmetic operations
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        result = print("the sum is: ", self.a+self.b)
        return result

    def sub(self):
        result = print("the sub is: ", self.a-self.b)
        return result

    def mul(self):
        result = print("the mul is: ", self.a*self.b)
        return result

    def divide(self):
        if self.b == 0:
            return "Error: Division by Zero"
        result = print("the div is: ", self.a / self.b)
        return result

a = int(input("Enter the 1st value:- "))
b = int(input("Enter the 2nd value:- "))

calc = Calculator(a, b)
calc.add()
calc.sub()
calc.mul()
calc.divide()
