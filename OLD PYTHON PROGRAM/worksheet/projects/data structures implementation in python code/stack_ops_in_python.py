l = []
while True:
    c = int(input('''
                1 PUSH ELEMENTS
                2 POP ELEMENTS
                3 PEEK ELEMENTS
                4 DISPLAY STACK
                5 EXIT
                '''))

    if c == 1:
        element = input("Enter the value:-")
        l.append(element)
        print(f"Entered value:-{element}""=>",l)

    elif c == 2:
        if len(l) == 0:
            print(f"empty stack:-{l}")
        else:
            p = l.pop()
            print("popped out element:-",p)
            print("modified list:-",l)

    elif c == 3:
        if len(l) == 0:
            print(f"empty stack:-{l} ")
        else:
            print("stack last value:-", l[-1])
    elif c == 4:
        print(f"display Stack:-{l}")
    
    elif c == 5:
        print("Invalid choice. Please enter a number between 1 and 5.")
        break;
