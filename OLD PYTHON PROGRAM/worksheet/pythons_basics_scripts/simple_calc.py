print('''
    ADD,
    DIVIDE,
    MULTIPLICATION,
    SUB,
    EXPONENT
''')

x = eval(input("enter your 1st number:- "))
y = eval(input("enter your 2nd number:- "))
operation = str(input("choose your operation to perform  on the two numbers:-")).lower()

if operation == "add":
    print("result:-", x + y)
elif operation == "div":
    print("result:-", x / y)
elif operation == "mul":
    print("result:-", x * y)
elif operation == "sub":
    print("result:-", x - y)
elif operation == "exp":
    print("result:-", x ** y)
else:
    print("invalid operation please try again")
