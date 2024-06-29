print("""
String methods used in the code:

* lower(): Converts the string to lowercase.
* upper(): Converts the string to uppercase.
* title(): Converts the string to title case (first letter of each word capitalized).
* capitalize(): Capitalizes the first letter of the string.
* find(): Finds the first occurrence of a character in the string.
* index(): Finds the first occurrence of a character in the string, raising an error if not found.
* isalpha(): Checks if all characters are alphabetic.
* isdigit(): Checks if all characters are digits.
* isalnum(): Checks if all characters are alphanumeric.
""")


# Assign the string "LOREM IPSUM IRO TURF" to the variable w
w = "LOREM IPSUM IRO TURF"

# Convert the string to lowercase and store it in variable u1
u1 = w.lower()
print("Lowercase:", u1)  # Print the lowercase string with a descriptive label

# Convert the string to uppercase and store it in variable u2
u2 = w.upper()
print("Uppercase:", u2)  # Print the uppercase string with a descriptive label

# Convert the string to title case and store it in variable u3
# Title case capitalizes the first letter of each word and leaves the rest lowercase
u3 = w.title()
print("Title case:", u3)  # Print the title case string with a descriptive label

# Capitalize the first letter of the string and store it in variable u4
u4 = w.capitalize()
# Print the capitalized string with a descriptive label
print("Capitalized:", u4)

# Find the first occurrence of the character 'I' in the string and print its index
print("Index of 'I':", w.find('I'))

# Find the first occurrence of the character 'F' in the string starting from index 2 and print its index
print("Index of 'F' after index 2:", w.find('F', 2))

# Find the first occurrence of the character 'R' in the string starting from index 2 and print its index
print("Index of 'R' with '.index'-function:", w.index('R', 2))

# Check if all characters are alphabetic
print("Is all alphabetic:", w.isalpha())

# Check if all characters are digits
print("Is all digits:", w.isdigit())

# Check if all characters are alphanumeric
print("Is all alphanumeric:", w.isalnum())
