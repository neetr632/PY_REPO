from collections import namedtuple

# Define a namedtuple type 'Point' with fields 'x' and 'y'
Point = namedtuple('Point', ['x', 'y'])

# Create an instance of Point
p1 = Point(1, 2)

# Accessing elements like a tuple
print(p1[0], p1[1])  # Output: 1 2

# Iterating over elements
for value in p1:
    print(value)  # Output: 1, then 2

# Accessing elements by name
print(p1.x, p1.y)  # Output: 1 2 #main difference between tuple and namedtuple

# Tuple methods
print(p1.index(2))  # Output: 1 (index of value 2 in the namedtuple)
