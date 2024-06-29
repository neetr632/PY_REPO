# Creating a tuple
tuple = (1, 3, 34, 234, 56, 23, 54, 24, 4672, 234)

# Finding the minimum value
m = min(tuple)

# Finding the maximum value
m1 = max(tuple)

# Counting the occurrences of 24
c = tuple.count(24)

# Finding the index of 34
d = tuple.index(34)

# Getting the element at index 3
u = tuple[3]

# Sum of the tuple
s = sum(tuple)

# Sum of tuple with 100 added
s_1 = sum(tuple, 100)

# Printing the results
print(f"Minimum value: {m}")
print(f"Value at index 3: {u}")
print(f"Index of 34: {d}")
print(f"Sum of tuple: {s}")
print(f"Added 100 to the sum of tuple: {s_1}")
print(f"Count of 24: {c}")
print(f"Maximum value: {m1}")

print("************************ New line ************************")
print("Questionnaire and doubts")
print("QUESTION-1==> Why are tuples ordered and immutable?")
print("""
Tuples are ordered and immutable for several reasons,
both technical and practical:""")
print("""
ANSWERS:

TECHNICAL REASONS:

1. **Memory efficiency:** By being ordered, tuples can be stored in memory contiguously, meaning all elements are located next to each other. This allows for faster access and efficient use of memory.
2. **Immutability guarantees data integrity:** Once created, a tuple cannot be modified. This ensures data consistency and prevents accidental changes.
3. **Simplified implementation:** Making tuples immutable simplifies their implementation in the Python interpreter, requiring less code and resources to manage.

PRACTICAL REASONS:

1. **Clarity and predictability:** Ordering elements in a tuple conveys their specific order and meaning, enhancing code clarity and predictability for other developers reading the code.
2. **Data security:** Immutability prevents accidental or malicious modification of data, making it a safe and reliable choice for storing sensitive information.
3. **Increased performance:** Immutability allows for optimizations in certain situations. For example, Python can pre-calculate the hash of a tuple once, knowing it will never change.
""")
