firstname = input("Enter the first name: ")
lastname = input("Enter the last name: ")

fullname = firstname + " " + lastname  # Add a space between first and last name

reversed_string = ""

for x in fullname:
    reversed_string = x + reversed_string

print("Reversed Name:", reversed_string)
