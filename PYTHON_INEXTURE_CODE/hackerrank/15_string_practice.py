# rows_1 = int(input())
rows = 21
cols = rows * 3
expression = ".|."

for i in range(rows // 2):
    print(((2 * i + 1) * expression).center(cols, "-"))
    
print("Welcome".center(cols, "-"))

# range(start, stop, step)
for i in range(rows // 2, 0, -1):
    print(((2 * i - 1) * expression).center(cols, "-"))
