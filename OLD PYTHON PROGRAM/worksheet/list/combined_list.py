# Create a mixed list containing integers, strings, boolean, float and list
my_list_1 = [1, "banana", True, 3.14, [1, 2, 3]]

# Print a sublist with step 3, starting from index 1 (inclusive)
# 1::3 means start from index 1 and include every 3rd element
print("my_list_1[1::3]:", my_list_1[1::3])  # Output: ["banana", [1, 2, 3]]
# ""::"" indicates the step-size for example :- [1::3] starting from index 1 (inclusive) and including every 3rd element thereafter.
# Print a sublist from index 1 to 3 (exclusive)
print("my_list_1[1:3]:", my_list_1[1:3])  # Output: ["banana", True]
# excluding 0th element and excluding the 3rd also only the middle elements are selected.
# Print a sublist from the beginning to index 3 (exclusive)
print("my_list_1[:3]:", my_list_1[:3])  # Output: [1, "banana", True]
# it signifies the default starting index of 0 (beginning) and an exclusive ending index like [:3].
# Print a sublist with step 3, starting from the beginning
print("my_list_1[::3]:", my_list_1[::3])  # Output: [1, 3.14]
# ""::"" indicates the step-size for example :- [::3] starting from index 0 (inclusive) and including every 3rd element thereafter  ``