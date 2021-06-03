END_COMMAND = "END"
SWAP_COMMAND = "swap"


def is_len_input_data_valid(user_input):
    if len(user_input) == 5:
        return True
    return False


def is_input_data_from_zero_index_swap(user_input1):
    if user_input1[0] == SWAP_COMMAND:
        return True
    return False


def is_indexes_valid(user_input2, input_r, input_c):
    row1 = int(user_input2[1])
    col1 = int(user_input2[2])
    row2 = int(user_input2[3])
    col2 = int(user_input2[4])
    if 0 <= row1 < input_r and 0 <= row2 < input_r and 0 <= col1 < input_c and 0 <= col2 < input_c:
        return True
    return False


rows, columns = [int(el) for el in input().split()]

matrix = []

for row in range(rows):
    matrix.append(input().split())

input_data = input()

while not input_data == END_COMMAND:
    command = input_data.split()
    if is_len_input_data_valid(command) and is_input_data_from_zero_index_swap(command) and \
            is_indexes_valid(command, rows, columns):
        row1 = int(command[1])
        col1 = int(command[2])
        row2 = int(command[3])
        col2 = int(command[4])
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(" ".join(el)) for el in matrix]
    else:
        print("Invalid input!")

    input_data = input()
