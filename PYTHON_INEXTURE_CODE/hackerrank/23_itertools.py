import itertools
a = input().split()
b = input().split()
A = list(map(int, a))
B = list(map(int, b))
AxB = itertools.product(A,B)
for item in AxB:
    print(item , end=" ") 
