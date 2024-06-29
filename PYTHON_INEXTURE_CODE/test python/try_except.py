number = int(input("enter the number:- "))
try:
    print(100/number)
except ValueError:
    print("Oops! That was no valid number.  Try again...")