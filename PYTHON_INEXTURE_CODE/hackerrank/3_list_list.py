list_1 = [["A",12],["B",32],["F",7] ,["G",67], ["H",7],["C",43], ["D",23] ,["E",64]]
sorted_list = sorted(list_1, key=lambda x:x[1]) 
print(sorted_list)
print(sorted_list[1])
for x in sorted_list:
    print(x[1]) 
    