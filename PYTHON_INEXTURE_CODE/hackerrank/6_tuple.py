n = int(input())
elements = input().split()
if len(elements) == n:
    tuple_elements = tuple(int(elem) for elem in elements)
    hash_value = hash(tuple_elements)
    print(hash_value)
else:
    print("Error")