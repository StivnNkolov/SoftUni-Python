def creating_initial_matrix(number):
    matrix = []
    for _ in range(number):
        curr_input = [int(el) for el in input().split()]
        matrix.append(curr_input)
    return matrix


def calculating_primary_diagonal_sum(data):
    primary_sum = 0
    for index in range(len(data)):
        primary_sum += data[index][index]
    return primary_sum


def calculating_secondary_diagonal_sum(data):
    secondary_sum = 0

    for index in range(len(data)):
        secondary_sum += data[index][len(data) - index - 1]
    return secondary_sum


def print_results(primary, secondary):
    result = abs(primary - secondary)
    print(result)


initial_matrix = creating_initial_matrix(int(input()))
primary_diagonal_sum = calculating_primary_diagonal_sum(initial_matrix)
secondary_diagonal_sum = calculating_secondary_diagonal_sum(initial_matrix)
print_results(primary_diagonal_sum, secondary_diagonal_sum)
