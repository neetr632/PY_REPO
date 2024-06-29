import random
for i in range(10):
    print(f"the loop is currently running at the index {i+1}")
    
icontains = None
print(type(icontains))

complex_1 = 3+5j
complex_2 = 1+5j
result = complex_2-complex_1
print(result)

random_string = "random string" 

"""list representations"""

squares_list = [x*x for x in range(10)]
print("list below is a square of numbers upto 10")
print(squares_list)

squares_list.pop()
print(f"pop out the last element of the squares_list:- {squares_list}")

squares_list.append(81)
print(f"the append adds elements to the last of the squares_list: {squares_list}")

squares_list.insert(1, 21)
print(f"the inserts elements at the given index of the squares_list: {squares_list}")

cube_list = [x**3 for x in range(10)]
print("list below is a cube of numbers upto 10")
print(cube_list)

'''extend methods can take any iterable to add the list for example list,strings,tuple etc'''
cube_list.extend([squares_list]) 
print(cube_list)
print(f"the list is the nested list of squares and cubes of the numbers upto 10 {cube_list}")

cube_list.extend([random_string]) 
print(f"the list is the nested list of squares and cubes and cubes of the numbers upto 10 {cube_list}")

list = [random.randint(1,5) for x in range(10)]
print(f"the numbers are randomly generated {list}")

cube_list.clear()
print(cube_list)

list.reverse()
print("reversed list",list)

copt = list.copy()
print(f"this is a shallow copy of the list:-{copt}")

count = list.count(2)
print(count)

list.sort()
print("the sorted random list:-",list)

list.sort(reverse=True)
print("the sorted reverse random list:-",list)

x__y_values = [(x,y) for x in range(3) for y in range(3) if x!=y]
print("x _ y values as a list of tuples:- ", x__y_values)
""" we can use the list as a "STACK" AND "QUEUE" try importing collections import deque used for fast popups and appends from both the ends """

odd_Even_list = [1,2,3,4,5,6,7,8,9]
odd_nums = [x for x in odd_Even_list if x %2!=0]
print("only odd numbers here:-",odd_nums)
