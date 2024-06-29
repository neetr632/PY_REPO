# Receive inputs for x, y, z, and n
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
n = int(input("Enter n: "))

# Calculate the sum of x, y, and z
prob_sum = x + y + z

# Generate triplets (i, j, k) where i < x, j < y, k < z and i + j + k != n
triplets = [(i, j, k) for i in range(x) for j in range(y) for k in range(z) if (i + j + k) != n]

# Print the generated triplets
print("Generated Triplets:", triplets)
