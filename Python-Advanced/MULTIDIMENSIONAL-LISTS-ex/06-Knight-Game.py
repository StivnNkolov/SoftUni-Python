n = int(input())

matrix = []

for row in range(n):
    matrix.append([el for el in input()])


def check_for_valid_index(*args):
    possible_r = args[0]
    possible_c = args[1]
    dimensions = args[2]
    if 0 <= possible_r < dimensions and 0 <= possible_c < dimensions:
        return True
    return False


def count_kills(data, row_index, col_index):
    kills = 0
    movement_rows = [-2, -2, 2, 2, 1, 1, -1, -1]
    movement_cols = [-1, 1, -1, 1, -2, 2, -2, 2]
    for index in range(len(movement_rows)):
        possible_row = row_index + movement_rows[index]
        possible_col = col_index + movement_cols[index]
        if check_for_valid_index(possible_row, possible_col, n):
            possible_position = data[possible_row][possible_col]
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
        knights_removed += 1
    else:
        break

print(knights_removed)
