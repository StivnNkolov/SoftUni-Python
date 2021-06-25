def get_magic_triangle(n):
    matrix = []

    for num in range(1, n + 1):
        matrix.append([1] * num)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if row - 1 > 0 and col - 1 >= 0:
                if col in range(row):
                    matrix[row][col] = matrix[row - 1][col - 1] + matrix[row - 1][col]
    return matrix

print(get_magic_triangle(6))