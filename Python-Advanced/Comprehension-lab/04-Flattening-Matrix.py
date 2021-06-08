rows = int(input())

matrix = []

for r in range(rows):
    matrix.append(input().split())

print(f'[{", ".join(" ".join(sub_matr for sub_matr in matrix_el) for matrix_el in matrix)}]')
