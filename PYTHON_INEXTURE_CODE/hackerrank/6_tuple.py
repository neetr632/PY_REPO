tuple = ()
x = int(input())
line_input = input().split()
for i in line_input:
    tuple = tuple + (int(i),)
print(tuple)
HasHed_value = hash(tuple)
print(HasHed_value)
