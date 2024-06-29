import random

another_list = [random.randint(1, 20) for _ in range(20)]
print(another_list)

for x in another_list:
    if x % 2 == 0:
        print(f" these are the even values:- {x}")

print("\n")

"""
    end is not a method but a keyword argument. 
    It specifies what should be printed at the end of the output. 
    By default, print adds a newline character (\n) at the end of the output. 
    However, you can change this behavior using the end parameter.
"""

print("new tuple created with a syntactic construct known as :- comprehension")
another_tuple = tuple((random.randint(1, 50) for _ in range(20)))
print(another_tuple)

half_tuple = len(another_tuple) // 2
for x in another_tuple[:half_tuple]:
    if x % 2 != 0:
        print(f"these are the odd values from the tuples:- {x}")


a_dict = {
    "a": 1,
    "b": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
}
print("dictionary_keys:")
for key in a_dict:
    print(key, end=" , ")
print("\n")
print("dictionary_with_keys,values")
for key, value in a_dict.items():
    print(f"KEY:{key} == VALUE:{value}")

#while looping 
num = 0
while (num <= 50):
        num += 1
        print(num, end=' ')
        
print("\n")

x = 0
while (x < len(another_list)):
    print(another_list[x], end=' ')
    x += 1
    
    
