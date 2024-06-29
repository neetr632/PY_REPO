# Define a class named 'student'
class Student:
    def __init__(self):
        # Initialize a private instance variable '__name' with an empty string
        self.__name = ""
    # Define a method 'getname' to get the value of the private variable '__name'
    def getname(self):
        return self.__name
    # Define a method 'setname' to set the value of the private variable '__name'
    def setname(self, name):
        self.__name = name

# Create an object 'obj' of the 'Student' class
obj = Student()
# Set the name using the 'setname' method
obj.setname("Testing") 
# Get the name using the 'getname' method
name = obj.getname()
# Print the value of the 'name' variable
print(name)
