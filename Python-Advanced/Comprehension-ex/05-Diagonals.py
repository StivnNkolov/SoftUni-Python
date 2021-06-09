square_matrix_size = int(input())

matrix = [[int(num) for num in input().split(", ")] for el in range(square_matrix_size)]
#
# for row in range(square_matrix_size):
#     curr_row = input().split(", ")
#     matrix.append(curr_row)

first = [matrix[index][index] for index in range(square_matrix_size)]
second = [matrix[index][len(matrix) - index - 1] for index in range(square_matrix_size)]

print(f"First diagonal: {', '.join(map(str, first))}. Sum: {sum(first)}")
print(f"Second diagonal: {', '.join(map(str, second))}. Sum: {sum(second)}")
