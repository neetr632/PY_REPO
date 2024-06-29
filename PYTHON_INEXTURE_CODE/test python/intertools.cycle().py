from itertools import cycle

for i in zip(range(21), cycle([1, 2, 3, 4, 5, 6])):
    print(i)