def edit_matrix_size_from_input():
    rows, columns = [int(el) for el in input().split(", ")]
    return rows, columns


def creating_our_matrix(r):
    m = []
    for r in range(r):
        input_data = [int(el) for el in input().split(", ")]
        m.append(input_data)
    return m


def calculating_sum_of_elements(data):
    sum_elements = 0
    size = len(data)
    for row in range(size):
        for el in range(len(data[0])):
            sum_elements += data[row][el]
    return sum_elements


rows_count, columns_count = edit_matrix_size_from_input()
matrix = creating_our_matrix(rows_count)
sum_of_all_elements = calculating_sum_of_elements(matrix)

print(sum_of_all_elements)
print(matrix)
