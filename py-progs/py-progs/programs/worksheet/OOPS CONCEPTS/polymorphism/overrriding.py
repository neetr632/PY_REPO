# Define a class named Ws
class Ws:
    # Define a method named displayinfo in the class Ws
    def displayinfo(self, name=''):
        print("Welcome to Wscubetech: " + name)

# Define a class named IIP, which inherits from Ws
class IIP(Ws):
    # Override the displayinfo method from the parent class (Ws)
    def displayinfo(self):
        # Call the displayinfo method of the parent class using super()
        super().displayinfo()
        # Print an additional message for the IIP class
        print("Welcome to IIP")

# Create an object (instance) of the IIP class
obj = IIP()
# Call the displayinfo method of the IIP class
obj.displayinfo()

# This is an example of function overloading since a function is having multiple arguments being passed to it
