# Creating a set
set_1 = {10, 2, 32, 47, 34, 234, 245, 23, 523, 523, 2}
print(f"Set 1: {set_1}")  # Prints the set

# Converting a list to a set
list = [1, 32, 525, 3, 6, 2334, 23, 4, 63, 234, 23]
s = set(list)
print(f"Set from list: {s}")  # Prints the set created from the list

# Adding an element to a set
set_1.add(40320)
print(f"Set 1 after adding element: {set_1}")  # Prints the set after adding 40320

# Removing an element using pop()
removed_element = set_1.pop()
print(f"Removed element: {removed_element}")  # Prints the removed element
print(f"Set 1 after removing element: {set_1}")  # Prints the set after removing element

# Removing elements using remove() and discard()
set_2 = {1, 2, 4, 5, 6, 8, 3, 2}
set_2.remove(2)  # Raises KeyError if element is not present
set_2.discard(4)  # Silently ignores if element is not present
print(f"Set 2 after removing elements: {set_2}")  # Prints the set after removing elements

# Clearing a set
set_2.clear()
print(f"Set 2 after clearing: {set_2}")  # Prints the empty set

# Adding elements from another collection using update()
set_3 = {1, 12, 34, 234, 2, 465, 6, 45, 36, 23, 63}
l = [30, 40, 60]
set_3.update(l)
print(f"Set 3 after updating with list: {set_3}")  # Prints the set after adding elements from the list

print("************************ New line ************************")
print("Questionaire and doubts")

# Question 1: Why are sets unordered and mutable?
print("""
Sets are unordered collections of unique elements, meaning they don't have a specific order and can't contain duplicates. This is due to several reasons, both technical and practical:

**Technical reasons:**

* **Hashing:** Sets rely heavily on hashing to determine element membership and optimize operations like membership testing and removal. Hashing algorithms generally produce unique values for unique elements, regardless of their order.
* **Memory efficiency:** Sets are typically implemented using hash tables, which store elements based on their hash values. This allows for fast access and insertion/deletion operations, but doesn't require maintaining any specific order.
* **Simplicity of implementation:** Implementing set operations like union, intersection, and difference is easier and more efficient without the need to manage element order.

**Practical reasons:**

* **Unordered data representation:** Sets often represent unordered concepts like sets of unique IDs, keywords, or tags. Maintaining order for such data would be unnecessary and potentially inefficient.
* **Flexibility and dynamism:** Sets can easily be modified by adding or removing elements, making them suitable for dynamic data scenarios. This flexibility wouldn't be possible if the order had to be preserved.
* **Focus on element uniqueness:** The main focus of sets is to ensure unique elements and allow efficient membership testing. Order plays a secondary role in this context.

""")

# Question 2: What is hashing and why is it necessary?
print("""
Hashing is the process of converting an input of any size (text, numbers, files, etc.) into a fixed-length value called a hash. This value acts as a unique identifier for the original input.

Imagine a vast library with countless books. Finding a specific book by its title would be incredibly time-consuming if you had to search each book individually.

Hashing offers a solution by assigning each book a unique identifier based on its title. This identifier, called a hash, allows you to quickly locate the desired book without needing to examine every single title.

Here's why hashing is necessary:

1. **Uniqueness:** Different inputs should ideally produce different hashes, ensuring accurate identification based on the hash.
2. **Fixed size:** Regardless of the input size, the hash output will always be unique.
""")

