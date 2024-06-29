
from itertools import compress


condition = [False,True,False,False,True,False,True,True,False,True]
another_list = range(1, 15)

for i in compress(another_list,condition):
    print(i , end=' ')