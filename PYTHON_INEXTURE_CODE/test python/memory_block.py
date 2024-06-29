x = 100
y = 100

print(id(x))  # Memory address of x
print(id(y))  # Memory address of y
print(x is y)  # True, since x and y point to the same cached object
a = 300
b = 300

print(id(a))  # Memory address of a
print(id(b))  # Memory address of b
print(a is b)  # False, since a and b are different objects
a = 3000
b = 3000

print(id(a))  # Memory address of a
print(id(b))  # Memory address of b
print(a is b)  # False, since a and b are different objects
a = 30022
b = 30023
c = 30024
d = 40024
e = 40025
f = 40026


print(id(a))  # Memory address of a
print(id(b))  # Memory address of b
print(id(c))  # Memory address of b
print(id(d))  # Memory address of b
print(id(e))  # Memory address of b
print(id(f))  # Memory address of b
print(a is b)  # False, since a and b are different objects
