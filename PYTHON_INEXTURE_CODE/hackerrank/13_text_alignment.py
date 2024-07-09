width = 1
for i in range(5):
    print(("H" * width).center(10, '-'))
    width += 2

for i in range(6):
    width = 5
    print(("H" * width).center(10, '-'))

for i in range(3):
    width = 26
    print(("H" * width).center(30, '-'))
    
for i in range(6):
    width = 5
    print(("H" * width).center(10, '-'))
width_reverse = 9
for i in range(5):
    print(("H" * width_reverse).center(10, '-'))
    width_reverse -= 2