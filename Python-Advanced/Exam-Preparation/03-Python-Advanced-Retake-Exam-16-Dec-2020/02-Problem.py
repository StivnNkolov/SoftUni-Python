searched_string = input()
size_of_the_matrix = int(input())

matrix = []
player_position = None
for row in range(size_of_the_matrix):
    current_row = [el for el in input()]
    matrix.append(current_row)
    if "P" in current_row:
        player_position = row, current_row.index("P")

player_turns = int(input())

left = (0, -1)
up = (-1, 0)
right = (0, +1)
down = (+1, 0)


for turn in range(player_turns):
    command = input()
    player_row = player_position[0]
    player_col = player_position[1]

    if command == "up":
        up_row, up_col = up
        next_row = player_row + up_row
        next_col = player_col + up_col
        if next_row in range(size_of_the_matrix) and next_col in range(size_of_the_matrix):
            if not matrix[next_row][next_col] == "-":
                searched_string += matrix[next_row][next_col]
                matrix[next_row][next_col] = "P"
                matrix[player_row][player_col] = "-"
                player_position = next_row, next_col
            else:
                matrix[next_row][next_col] = "P"
                matrix[player_row][player_col] = "-"
                player_position = next_row, next_col
        else:
            if searched_string:
                searched_string = searched_string[:-1]
    elif command == "right":
        right_row, right_col = right
        next_row = player_row + right_row
        next_col = player_col + right_col
        if next_row in range(size_of_the_matrix) and next_col in range(size_of_the_matrix):
            if not matrix[next_row][next_col] == "-":
                searched_string += matrix[next_row][next_col]
                matrix[next_row][next_col] = "P"
                matrix[player_row][player_col] = "-"
                player_position = next_row, next_col
            else:
                matrix[next_row][next_col] = "P"
                matrix[player_row][player_col] = "-"
                player_position = next_row, next_col
        else:
            if searched_string:
                searched_string = searched_string[:-1]
    elif command == "down":
        down_row, down_col = down
        next_row = player_row + down_row
        next_col = player_col + down_col
        if next_row in range(size_of_the_matrix) and next_col in range(size_of_the_matrix):
            if not matrix[next_row][next_col] == "-":
                searched_string += matrix[next_row][next_col]
                matrix[next_row][next_col] = "P"
                matrix[player_row][player_col] = "-"
                player_position = next_row, next_col
            else:
                matrix[next_row][next_col] = "P"
                matrix[player_row][player_col] = "-"
                player_position = next_row, next_col
        else:
            if searched_string:
                searched_string = searched_string[:-1]
    elif command == "left":
        left_row, left_col = left
        next_row = player_row + left_row
        next_col = player_col + left_col
        if next_row in range(size_of_the_matrix) and next_col in range(size_of_the_matrix):
            if not matrix[next_row][next_col] == "-":
                searched_string += matrix[next_row][next_col]
                matrix[next_row][next_col] = "P"
                matrix[player_row][player_col] = "-"
                player_position = next_row, next_col
            else:
                matrix[next_row][next_col] = "P"
                matrix[player_row][player_col] = "-"
                player_position = next_row, next_col
        else:
            if searched_string:
                searched_string = searched_string[:-1]


print(searched_string)
[print(*el, sep="") for el in matrix]
