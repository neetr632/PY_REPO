first_number, second_number = map(
    int, input("enter the first number and second number: ").split()
)
print(first_number)
print(type(first_number))
print(second_number)
print(type(second_number))
if first_number is second_number:
    print("numbers are equal")
else:
    print("numbers are not equal")


