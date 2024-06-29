from itertools import starmap

def add(a , b):
    return a + b
#when you want to map different iterables as a list to a function for that starmap() is used to map them to a function

groupings = [(1,4),(3,5),(2,6),(7,8),(9,10)]

result = starmap(add, groupings)
print(list(result))