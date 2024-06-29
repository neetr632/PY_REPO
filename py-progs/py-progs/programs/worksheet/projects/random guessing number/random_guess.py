import random
Cnumber = random.randrange(1,101)
while True:
    userInput = int(input("Enter your number:---"))
    if userInput==Cnumber:
        print("congratulations your number is correct")
    elif userInput>Cnumber:
        print("your number is too high")
    elif Cnumber>userInput:
        print("your number is too low")
    else:
        print("try again!! you failed")