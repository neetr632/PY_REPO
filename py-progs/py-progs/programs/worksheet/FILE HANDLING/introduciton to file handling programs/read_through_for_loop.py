# Import the `time` module for using its sleep function
import time
# Open the file "random_text.txt" in read mode and assign it to `file`
file = open("random_text.txt", "r")
# Read the entire contents of the file into a string variable `x`
x = file.read()
# Initialize a variable `count` to keep track of the number of characters
count = 0
# Iterate over each character in the string `x`
for ch in x:
    # Print the current character without a newline and update the count
    print(ch, end="")
    count += 1
    # Add a short delay after each character (optional)
    time.sleep(0.01)
# Print the total number of characters on a new line
print("\nthe number of characters in the text file is :- ", count)
# Close the file to release resources
file.close()
