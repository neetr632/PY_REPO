with open ("worksheet_1.txt") as input_file:
    while True:
        line = input_file.readline()
        if not line:
            break
        print(line.strip())
        
with open("worksheet_1.txt") as input_file:
    x = " "
    while x:
        x = input_file.readlines()
        print(x,end="")
    
             