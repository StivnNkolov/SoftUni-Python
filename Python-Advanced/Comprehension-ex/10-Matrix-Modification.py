def is_indexes_valid(r_index, c_index, data):
    if 0 <= r_index < len(data) and 0 <= c_index < len(data):
        return True
    return False


input_rows_count = int(input())

# matrix = []
#
# for r in range(input_rows_count):
#     matrix.append([int(el) for el in input().split()])

matrix1 = [[int(num) for num in input().split()] for el in range(input_rows_count)]

input_command = input()

while not input_command == "END":
    command_data = input_command.split()
    command_type = command_data[0]
    row_index = int(command_data[1])
    column_index = int(command_data[2])
    value = int(command_data[3])
    if is_indexes_valid(row_index, column_index, matrix1):
        if command_type == "Add":
            matrix1[row_index][column_index] += value
        elif command_type == "Subtract":
            matrix1[row_index][column_index] -= value
    else:
        print("Invalid coordinates")

    input_command = input()

[print(*el) for el in matrix1]
