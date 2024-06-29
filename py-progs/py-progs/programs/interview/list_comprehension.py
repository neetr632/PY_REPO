list = [i ** 3 for i in range(10)]
with open("list.txt", 'w') as f:
    f.write(str(list))

print("done writing to the file")

print(list.count(27))
list.append(23)
print(list)
list.reverse()
print(list)


def x(x): return x + 1


y = x(5)
print("usage of lambda function multiplication: ", y)


def a(x, y): return x**y


print("lambda function multiplication: ", a(2, 4))


def hello(): return "hello, world!"


# the parentheses are used to call the function iterable of the lambda function.
print("simple hello from the lambda function", hello())
"""
    lambda is a anonymous function that can take multiple arguments but 
    only one expression can be defined in it
"""
# What is the difference between / and // in Python?

float_divide = lambda x,y : x/y
print("floor_division: ",float_divide(5,2))

int_divide = lambda x,y : x//y # represents floor division
print("int_divide",int_divide(5,2)) # represents precision division 