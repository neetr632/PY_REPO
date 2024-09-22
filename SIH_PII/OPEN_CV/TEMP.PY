import numpy as np
def create_arr():
    number = []
    dim = input("").strip().split(" ")
    row, col = int(dim[0]), int(dim[1])
    for _ in range(row):
        num = input("").strip().split(" ")
        num = list(map(int, num)) # use of map to convert the ind. ele to int
        number.append(num)
    rex = np.array(number)  
    rex_arr_1 = rex.T  
    rex_arr_2 = rex.flatten()  
    return rex_arr_1, rex_arr_2
rex_arr_1, rex_arr_2 = create_arr()
print(rex_arr_1)
print(rex_arr_2)
