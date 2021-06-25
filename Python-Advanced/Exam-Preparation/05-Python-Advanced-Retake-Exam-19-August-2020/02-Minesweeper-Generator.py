import re


def check_for_bomb(board, curr_row, curr_col):
    number = 0
    look_around_places = ((0, -1), (-1, -1), (-1, 0), (-1, +1), (0, +1), (+1, +1), (+1, 0), (+1, -1))
    for location in look_around_places:
        if 0 <= curr_row + location[0] < len(board) and 0 <= curr_col + location[1] < len(board):
            if board[curr_row + location[0]][curr_col + location[1]] == "*":
                number += 1
    return number


input_number_for_size = int(input())
input_number_of_bombs = int(input())

playing_field = [[f"." for sm in range(input_number_for_size)] for el in range(input_number_for_size)]
pattern = r"\d"
for bomb in range(input_number_of_bombs):
    input_location = input()
    bomb_locations = (re.findall(pattern, input_location))
    index_1 = int(bomb_locations[0])
    index_2 = int(bomb_locations[1])
    if 0 <= index_1 < len(playing_field) and 0 <= index_2 and len(playing_field):
        playing_field[index_1][index_2] = "*"

for row in range(len(playing_field)):
    for col in range(len(playing_field)):
        if not playing_field[row][col] == "*":
            playing_field[row][col] = check_for_bomb(playing_field, row, col)
        else:
            continue
[print(*el) for el in playing_field]
