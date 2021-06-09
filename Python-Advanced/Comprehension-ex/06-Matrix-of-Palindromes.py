input_rows, input_cols = map(int, input().split())

# matrix = [[f"{chr(number)}{chr(nested_num)}{chr(number)}" for nested_num in range(number, number + input_cols)] for
#           number in range(97, 97 + input_rows)]
#
# [print(*el) for el in matrix]

matrix2 = []
for r in range(input_rows):
    curr_list = []
    for c in range(input_cols):
        curr_result = f"{chr(97+r)}{chr(97+r+c)}{chr(97+r)}"
        curr_list.append(curr_result)
    matrix2.append(curr_list)

[print(*el) for el in matrix2]