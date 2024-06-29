class A:
    def method_A(self):
        print("Method A from class A")

class B:
    def method_B(self):
        print("Method B from class B")

class C(A, B):
    def method_C(self):
        print("Method C from class C")

# Creating an instance of class C
obj = C()

# Accessing methods from class A
obj.method_A()

# Accessing methods from class B
obj.method_B()

# Accessing method from class C
obj.method_C()
