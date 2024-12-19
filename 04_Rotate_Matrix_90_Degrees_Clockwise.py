def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate_matrix(matrix)
print("Rotated matrix:")
for row in matrix:
    print(row)
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
