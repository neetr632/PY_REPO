def square(*args):
    numbers = []
    for arg in args:
        numbers.append(arg*arg)
    return numbers

result = square(1,2,3,4,5,6,7,8)
print(result)
cube_numbers = list(map(square, result))
print(f"the cube of the same numbers are:{cube_numbers}")

