class Example:
    def __init__(self, name,):
        self.name = name
        self.__private_method = 10

obj = Example("bob")
print(obj.name)
# print(obj.__private_method)
print(
    f"accessing the private attributes in the class that are not meant to be manipulated accidentally: {obj._Example__private_method}"
)
