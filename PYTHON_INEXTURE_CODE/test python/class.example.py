class Example:
    def __init__(self, name):
        self.name = name
        self.name = "Jhon"

    def call_me(self):
        print("hello")
        return "returned hello successfully"


obj = Example("bob")
call_object = obj.call_me
print(call_object())

instance_1 = Example("alice")
print(
    instance_1.name
)  # instance is used to use the same code with different data with the same code. used to create individual objetcs with thier own data(attributes) and behaviour(methods)
