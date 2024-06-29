# By using the format function, we can insert any value between a string

# "lorem {} ipsum turf {} aro" is a template string with two placeholders
w = "lorem {} ipsum turf {} aro".format(
    # Replace the first placeholder with "hello this is disturbing i know"
    "hello this is disturbing i know",
    # Replace the second placeholder with the integer 20334
    20334
)
print(w)  # Print the formatted string

# "abcd {0} efghi {1} jklmno {2} pqrst {3} uvwxy" is another template string with five placeholders
y = "abcd {0} efghi {1} jklmno {2} pqrst {3} uvwxy".format(
    # Replace the placeholders with the corresponding integers
    123,
    12234,
    3453,
    32452
)
print(y)  # Print the formatted string

# "welcome to {a:4} the {b:^4} program" is another template string with two named placeholders
z = "welcome {a:>4} to {a:4} the {b:^4} program{b:<4}".format(
    # Use keyword arguments to replace placeholders
    a=23,
    b=34
)
print(z)  # Print the formatted string

# The format specifiers "{:4}" and "{:^4}" are used to control the width and alignment of the values
# "{:4}" formats the value to a minimum width of 4 characters and right-aligns it
# "{:^4}" formats the value to a minimum width of 4 characters and centers it
# "{:>4}" formats the value to a minimum width of 4 characters and right-aligns it
# "{:<4}" formats the value to a minimum width of 4 characters and left-aligns it