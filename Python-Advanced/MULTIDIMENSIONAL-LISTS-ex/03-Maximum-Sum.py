rows, columns = [int(el) for el in input().split()]

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

max_sum = 0
coordinates = []
for r in range(rows - 2):
    for c in range(columns - 2):
        first_row = [matrix[r][c], matrix[r][c + 1], matrix[r][c + 2]]
        second = [matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2]]
        third = [matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2]]
        total_sum = sum(first_row) + sum(second) + sum(third)
        if total_sum >= max_sum:
            max_sum = total_sum
            coordinates = [first_row, second, third]

print(f"Sum = {max_sum}")
for el in coordinates:
    print(" ".join([str(el) for el in el]))

