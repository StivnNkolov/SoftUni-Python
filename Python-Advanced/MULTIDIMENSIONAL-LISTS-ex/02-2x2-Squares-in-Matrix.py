def create_initial_matrix(input_r):
    initial_matrix = []
    for r in range(input_r):
        input_data = input().split()
        initial_matrix.append(input_data)
    return initial_matrix


def find_boxes_with_equal_values(data):
    equal_squares = []
    start_row = 0
    start_column = 0

    while start_row < row_number - 1:
        curr_list = []
        for row in range(2):
            for c in range(2):
                curr_el = data[start_row + row][start_column + c]
                curr_list.append(curr_el)
        char = curr_list[0]
        if curr_list.count(char) == 4:
            equal_squares.append(curr_list)
        start_column += 1
        if start_column == column_number - 1:
            start_row += 1
            start_column = 0
    return equal_squares


def print_result(equal_data):
    if equal_data:
        print(len(equal_data))
    else:
        print("0")


row_number, column_number = [int(el) for el in input().split()]
matrix = create_initial_matrix(row_number)
equal_cells = find_boxes_with_equal_values(matrix)
print_result(equal_cells)

