list = []
while True:
    c = int(input('''
                1 PUSH ELEMENT TO THE LAST OF THE QUEUE
                2 POP THE ELEMENT FROM THE LAST
                3 PEEK ELEMENTS
                4 DISPLAY STACK INDEX '0' VALUE
                5 EXIT
                '''))
    if c == 1:
        element = input("ENTER THE VALUE:-")
        list.append(element)
        print(f"ENTERED VALUE:-{element}""=>",list)

    elif c == 2:
        if len(list) == 0:
            print(f"EMPTY LIST:-{list}")
        else:
            popped_element = list.pop()
            print("POPPED OUT ELEMENT:-",popped_element)
            print("MODIFIED LIST:-",list)

    elif c == 3:
        if len(list) == 0:
            print(f"EMPTY LIST:-{list} ")
        else:
            print("STACK LAST VALUE:-", list[-1])
    
    elif c == 4:
        print(f"DISPLAY STACK's INDEX 0 VALUE:-",list[0])
    
    elif c == 5:
        print("INVALID CHOICE. PLEASE ENTER A NUMBER BETWEEN 1 AND 5.")
        break;
    
    elif c == 6:
        if len(list)==0:    
            print("EMPTY LIST")
        else:
            print("THE CURRENT STACK IS:-",list)
    else:
        print("ENTER A VALID INPUT AND TRY AGAIN")
        break; 
