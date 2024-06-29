# list_comprehensions
x = int(input())
y = int(input())
z = int(input())
n = 3
triplets = [(i, j, k) for i in range(x) for j in range(y) for k in range(z) if (i + j + k) != n]
print(triplets)
