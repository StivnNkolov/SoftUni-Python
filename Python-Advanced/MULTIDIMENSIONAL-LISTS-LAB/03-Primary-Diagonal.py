# to find the sum of an y diagonal the matrix has to be square

def calculating_primary_diagonal_sum(data):
    matrix_size = len(data)
    primary_d_sum = 0
    for index in range(matrix_size):
        primary_d_sum += data[index][index]
    return primary_d_sum


def creating_our_square_matrix(number):
    square_matrix = []
    for row in range(number):
        column_values_from_input = [int(el) for el in input().split()]
        square_matrix.append(column_values_from_input)
    return square_matrix


matrix = creating_our_square_matrix(int(input()))
print(calculating_primary_diagonal_sum(matrix))
