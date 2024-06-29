
x = int(input())
y = int(input())
z = int(input())
n = int(input())
triplets = [(i, j, k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i + j + k) != n]
print(triplets)


# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], 
# [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], 
# [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]