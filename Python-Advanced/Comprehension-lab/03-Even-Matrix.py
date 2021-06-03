rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([el for el in [int(el) for el in input().split(", ")] if el % 2 == 0])

print(matrix)
