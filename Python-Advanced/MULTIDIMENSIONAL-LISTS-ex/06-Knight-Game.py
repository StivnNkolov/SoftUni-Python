n = int(input())

matrix = []

for row in range(n):
    matrix.append([el for el in input()])


def count_kills(matr, row_index, col_index):
    kills = 0
    movement_rows = [-2, -2, 2, 2, 1, 1, -1, -1]
    movement_cols = [-1, 1, -1, 1, -2, 2, -2, 2]
    for index in range(len(movement_rows)):
        possible_row = row_index + movement_rows[index]
        possibler_col = col_index + movement_cols[index]
        if 0 <= possible_row < len(matrix) and 0 <= possibler_col < len(matrix):
            possible_position = matrix[possible_row][possibler_col]
            if possible_position == "K":
                kills += 1

    return kills


knights_removed = 0
while True:
    max_kills = 0
    killer_position = []
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == "K":
                kills = count_kills(matrix, r, c)
                if max_kills < kills:
                    max_kills = kills
                    killer_position = [r, c]
    if killer_position:
        matrix[killer_position[0]][killer_position[1]] = "0"
        # killer_position = []
        knights_removed += 1
    else:
        break

print(knights_removed)
