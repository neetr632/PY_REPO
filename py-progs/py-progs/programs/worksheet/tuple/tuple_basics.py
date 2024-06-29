print("""
A tuple is an ordered sequence of elements, enclosed in parentheses.
Ordered: 
Immutable: 
Can contain duplicates:
Can contain any data type: 
""")
my_range = range(11)
my_tuple = tuple(my_range)
tuple = (1,3,34,234,56,23,54,24,4672,234)
print(my_tuple)

for a in tuple:
    print(a)
    
t = len(my_tuple)
for a in range(t):
    print(a)