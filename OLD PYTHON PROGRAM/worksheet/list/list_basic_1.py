list = [1, 3, 43, 2, 524, 3, 456, 564]

# Print sublist from index 1 (inclusive) to 5 (exclusive)
print("list[1:5]:", list[1:5])  # Output: [3, 43, 2, 524]

# Print sublist from the beginning (index 0) to 5 (exclusive)
print("list[:5]:", list[:5])  # Output: [1, 3, 43, 2, 524]

# Print sublist from index 5 (inclusive) to the end
print("list[5:]:", list[5:])  # Output: [3, 456, 564]

# Print sublist from the beginning to the last element (excluding)
print("list[:-1]:", list[:-1])  # Output: [1, 3, 43, 2, 524, 3, 456]

# Print sublist from index 2 (inclusive) to the last element (excluding)
print("list[2:-1]:", list[2:-1])  # Output: [43, 2, 524, 3, 456]
