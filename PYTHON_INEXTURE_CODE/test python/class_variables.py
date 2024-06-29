# The code defines two classes, A with a class variable and a class method, and B with an instance
# variable and a method to set its value.
class A:
    a = 10  # class_variable

    @classmethod
    def setvalue(cls):
        print(cls.a)


A.setvalue()


class B:
    def __init__(self):
        self.value = None

    def setvalue(self, value):  # instance method created
        self.value = value
        print(self.value)


object_1 = B()
object_1.setvalue(45)


class B:
    def __init__(self, value):
        self.value = value
        print(self.value)  # 20 value passed to the class ends here after getting printed

    def setvalue(self ):  # instance method created #value=45 as passed to the method while calling the object
        print(self.value)


object_1 = B(20)
object_1.setvalue()
