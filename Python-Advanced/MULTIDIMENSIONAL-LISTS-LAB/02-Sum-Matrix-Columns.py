def print_result(data):
    [print(el) for el in data]


def get_column_sum(data):
    rows_size = len(data)
    columns_size = len(data[0])
    columns_sums = []
    for c in range(columns_size):
        current_column_sum = 0
        for r in range(rows_size):
            current_column_sum += matrix[r][c]
        columns_sums.append(current_column_sum)
    return columns_sums


def edit_matrix_size_from_input():
    rows, columns = [int(el) for el in input().split(", ")]
    return rows, columns


def creating_our_matrix(r):
    m = []
    for r in range(r):
        input_data = [int(el) for el in input().split()]
        m.append(input_data)
    return m


rows_count, column_count = edit_matrix_size_from_input()
matrix = creating_our_matrix(rows_count)
all_columns_sums = get_column_sum(matrix)
print_result(all_columns_sums)
