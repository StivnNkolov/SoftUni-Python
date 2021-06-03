rows, columns = [int(el) for el in input().split()]

matrix = []
for i in range(rows):
    matrix.append([])
    for j in range(columns):
        matrix[i].append(0)

input_data = input()
index_for_element = 0

for r in range(1, rows + 1):
    if not r % 2 == 0:
        for c in range(columns):
            matrix[r - 1][c] = input_data[index_for_element]
            index_for_element += 1
            if index_for_element == len(input_data):
                index_for_element = 0
    else:
        for c1 in range(columns - 1, -1, -1):
            matrix[r - 1][c1] = input_data[index_for_element]
            index_for_element += 1
            if index_for_element == len(input_data):
                index_for_element = 0

[print("".join(el)) for el in matrix]

