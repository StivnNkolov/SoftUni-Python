rows, columns = [int(el) for el in input().split()]

matrix = []

input_string = input()
rowzz = input_string
for r in range(1, rows + 1):
    if not len(input_string) < columns:
        curr_row = rowzz[:columns]
        leftover = rowzz[columns:]
        if not r % 2 == 0:
            matrix.append(curr_row)
        else:
            matrix.append(curr_row[::-1])

        rowzz = leftover + curr_row
    else:
        diff = columns - len(input_string)
        leftover = input_string[diff:]
        if not r % 2 == 0:
            matrix.append(input_string + input_string[:diff])
        else:
            matrix.append((leftover + input_string)[::-1])

[print(el) for el in matrix]

