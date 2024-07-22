import numpy as np
def create_matrix():
    dimensions = input().split()
    rows, cols = int(dimensions[0]), int(dimensions[1])
    matrix_values = []
    for _ in range(rows):
        row_values = list(map(int, input().split()))
        if len(row_values) != cols:
            print(f"Warning: Expected {cols} values, but received {len(row_values)}. Please try again.")
            return None, None  
        matrix_values.append(row_values)
    k = int(input())
    matrix = np.array(matrix_values)
    return matrix, k  

def sort_matrix_by_column(matrix, k):
    sort_indices = np.argsort(matrix[:, k])
    sorted_matrix = matrix[sort_indices]
    return sorted_matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

matrix, k = create_matrix()

if matrix is not None:
    sorted_matrix = sort_matrix_by_column(matrix, k)
    print_matrix(sorted_matrix)
