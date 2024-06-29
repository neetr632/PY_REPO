def func(x , y):
    return x + y

result = func(2,4)
print(result)
another = func # Reference To The Func.
print(f"here the function is passed as objects:{another}")
another_result = another(2, 5)
print(another_result)

print("-------------------------------------------------------------------------------------")

