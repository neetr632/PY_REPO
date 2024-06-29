from itertools import islice

T3_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
T3_numbers = islice(T3_numbers, 3)
print(list(T3_numbers))
