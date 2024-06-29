# Creating a set
my_set = {1, 2, 3}

# Adding elements using add()
my_set.add(4)  # Adds 4 to the set
my_set.add(5)  # Adds 5 to the set
my_set.add(2)  # Doesn't add 2 again (duplicate)

# Adding elements using update()
my_list = [6, 7, 8]
my_set.update(my_list)  # Adds 6, 7, and 8 to the set

# Printing the updated set
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
