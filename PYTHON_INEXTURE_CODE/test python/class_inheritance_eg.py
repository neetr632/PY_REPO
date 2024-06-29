class ArithmeticOperations:
    def add(self, a, b):
        return self.a + self.b

    def sub(self, a, b):
        return self.a - self.b


class AdvancedOperations(ArithmeticOperations):
    def multiply(self, a, b):
        return self.a * self.b

    def divide(self, a, b):
        return self.a / self.b

obj = AdvancedOperations(10,42)
print(f"the values are of the class that was inherited{obj.add()}")
print(f"the values are of the class that was inherited{obj.multiply()}")
print(f"the values are of the class that was inherited{obj.sub()}")
print(f"the values are of the class that was inherited{obj.divide()}")