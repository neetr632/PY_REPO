def gen_function(value):
    for char in value:
        yield char


gen = gen_function("101010101110000111")
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator function in a for loop
for num in countdown(5):
    print(num)
