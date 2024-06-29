class DemoClass:
    a = 10

    def sumValue(self, x=21, y=24):  # self works an argument itself.
        return x + y


demoObject = DemoClass()  
# object can call any methods and variables of the class.
# multiple objects can be created of a single class.
print(f"a class variable is printed here:- {demoObject.a}")
print(f"results from the function object with custom values:- {demoObject.sumValue(10, 20)}")
print(f"result with the preset values in the function object:- {demoObject.sumValue()}")
