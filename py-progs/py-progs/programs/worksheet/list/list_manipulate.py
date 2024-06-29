# List of integers
x = [10, 123, 24, 234, 45, 23, 67, 43556]

# Delete element 1 (index 0)
del x[0]
print("Element 1 is deleted:", x)  # Output: [123, 24, 234, 45, 23, 67, 43556]

# List of integers
y = [1, 2, 4, 5, 6, 7, 8, 3, 2]

# Pop element at index 2 (third element)
y.pop(2)
print("Element at index 2 is popped:", y)  # Output: [1, 2, 5, 6, 7, 8, 3, 2]

# List of integers
z = [1, 43, 24, 314, 2344, 46, 231]

# Remove element with value 231
z.remove(231)
print("Element 231 is removed by value:", z)  # Output: [1, 43, 24, 314, 2344, 46]

# List of integers
t = [12, 123, 2, 4, 234, 123, 12, 345]

# Clear all elements from the list
t.clear()
print("All elements are deleted:", t)  # Output: []

# List of integers
u = [1, 2, 42, 435, 67, 4, 8, 245]

# Insert element 1233 at index 2
u.insert(2, 1233)
print(u)  # Output: [1, 2, 1233, 42, 435, 67, 4, 8, 245]

# List of integers
r = [1, 23, 4, 2, 4, 3]

# Append element 195 and another list u
r.append(195)
r.append(u)
# Extend the list with the elements of list x
r.extend(x)
r.insert(0,100000) # insert 100000 at index 0
print(r)  # Output: [1, 23, 4, 2, 4, 3, 195, [1, 2, 1233, 42, 435, 67, 4, 8, 245], 10, 123, 24, 234, 45, 23, 67, 43556]
