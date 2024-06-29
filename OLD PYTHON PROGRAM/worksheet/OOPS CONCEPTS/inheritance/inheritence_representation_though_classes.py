# Define Class A
class A:
    def __init__(self):
        print("Quick way to represent inheritance with two classes A and B.")
        print("Class B's object named 'demoObj' is calling methods of both classes A and B.")
    
    def display_a(self):
        print("This is Class A.")
        
# Define Class B, inheriting from Class A
class B:
    def display_b(self):
        print("This is Class B.")

class C(A,B):
    def display_c(self):
        print("this is class C")
# Create an object of Class B
demo_obj = C()

# Call methods from both Class A and Class B
demo_obj.display_a()
demo_obj.display_b()
demo_obj.display_c()
