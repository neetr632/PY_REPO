list_12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(list_12[0])  # This will print the first element of list_12

Sorted_list = [['F', 7], ['H', 7], ['A', 12], ['D', 23], ['B', 32], ['C', 43], ['E', 64], ['G', 67]]
Sorted_list.sort(reverse=True)
print(Sorted_list)
length = len(Sorted_list)  # This calculates the length of Sorted_list, which is 8

list_23 = [x for x in range(8)]  # This creates a list of numbers from 0 to 7
list_24 = [x for x in range(length - 1)]  # This creates a list of numbers from 0 to 6 

print(list_23)  # This will print list_23
print(list_24)  # This will print list_24
