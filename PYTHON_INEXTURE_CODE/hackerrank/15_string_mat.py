c = ".|."
x, y = map(int, input().split()) # Since the output is in odd numbers the middle line will be used to print the Welcome Message

for i in range(x // 2):
    line = "-" * (y // 2 - 3 * i) + c * (2 * i + 1) + "-" * (y // 2 - 3 * i)
    print(line.center(y, "-"))
    
print("WELCOME".center(y, "-"))

for i in range(x // 2 - 1, -1, -1):
    line = "-" * (y // 2 - 3 * i) + c * (2 * i + 1) + "-" * (y // 2 - 3 * i)
    print(line.center(y, "-"))
