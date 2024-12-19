def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Transposed matrix:", transpose(matrix))
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
