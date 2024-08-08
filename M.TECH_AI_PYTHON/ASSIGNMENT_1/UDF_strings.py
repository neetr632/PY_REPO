print("Here we are finding 'Y' in 'X' so enter the value accordingly")
x_string = str(input("Enter the 'X' string:- "))
y_string = str(input("Enter the 'Y' string:- "))
length_x = len(x_string)
print(f"Length of the 'X' string {length_x}")
length_y = len(y_string)

def find_same_String(x,y):
    start = 0
    end_value = 0
    indices = []
    while True:
        start = x.find(y, start)
        if start == -1:
            break
        end_value = start + len(y)
        indices.append((start, end_value))
        start += len(y)
    found = len(indices) > 0
    return indices, found
result, found = find_same_String(x_string,y_string)
print(f"the list with Start and end Index of the occurrences:- {result}")
print(f"Occurrences are found:- {found}")