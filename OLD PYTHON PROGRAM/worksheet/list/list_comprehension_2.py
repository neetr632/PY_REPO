# Generate a list of numbers from 1 to 20 using list comprehension
n = [m for m in range(1, 21)]

# Count the occurrences of the number 2 in the list
a = n.count(2)

# Find the maximum value in the list
m = max(n)
o = min(n)
# Print the maximum value and the count of 2
print("The maximum value in the list is: ", m)
# Print the minimum value and the count of 2
print("The minimum value in the list is: ", o)
print("The number 2 appears ", a, " times in the list.")
print("The list generated using a for loop is: ", n)

# Create a new list with unsorted elements
jk = [13, 436, 45, 8, 65]

# Sort the list in ascending order
jk.sort()

# Print the sorted list
print("The list sorted in ascending order is: ", jk)

# Reverse the order of the sorted list
jk.reverse()

# Print the reversed list
print("The reversed list is: ", jk)

# Find the index of the number 45 in the original list
lk = jk.index(45)

# Print the index of the number 45
print("The index of the number 45 is: ", lk)
