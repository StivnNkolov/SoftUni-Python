matrix = [
    [2, 3, 4],
    [1, "a", 5],
    [8, 7, 6]
]

a_row = 1
a_col = 1

print(matrix[a_row + 0][a_col + -1])
print(matrix[a_row + -1][a_col + -1])
print(matrix[a_row + -1][a_col + 0])
print(matrix[a_row + -1][a_col + +1])
print(matrix[a_row + 0][a_col + +1])
print(matrix[a_row + +1][a_col + +1])
print(matrix[a_row + +1][a_col + 0])
print(matrix[a_row + +1][a_col + -1])