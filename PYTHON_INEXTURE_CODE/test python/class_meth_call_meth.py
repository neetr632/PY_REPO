class Myclass:
    def __init__(self, name):
        self.name = name

    def method_1(self):
        print("method 1 called is being called by method_2")
        self.method_2()
        return "Method 1 called successfully by Method_2"

    def method_2(self):
        print("method 2 called is being called by method_1")
        return "Method 2 called successfully by Method_1"


object_for_calling_the_Class = Myclass("Bobby")
print(object_for_calling_the_Class.name)
object_for_calling_the_Class.method_1()
        