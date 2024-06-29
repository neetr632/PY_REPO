class Example:
    def __init__(self):
        self._private_var = 10  # to signal the developers that this is for internal use and somewhat external use is allowed from it.
        self.__private_var = 10  # private attribute used to prevent manipulation in the variable from outside the class

    def get_private_var(self):
        return self._private_var

obj = Example() #object of the class is created to access the methods.
print(obj.get_private_var())  # Output: 10.
# Direct access is possible, but conventionally discouraged
print(obj._private_var)  # Output: 10 #_private_var is a hint to other developers that the attribute should be treated as private
print(obj._Example__private_var) # __private_var is more about avoiding accidental name clashes and somewhat restricting external access.
