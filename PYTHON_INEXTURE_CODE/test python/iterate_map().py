def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = map(square, numbers)
print(list(squared_numbers))
