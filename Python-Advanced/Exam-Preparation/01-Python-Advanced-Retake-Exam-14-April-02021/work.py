import re

BOARD_SIZE = 7


def print_result(name, player_turns):
    print(f"{name} won the game with {player_turns} throws!")


def check_for_b(r_index, col_index, board):
    if board[r_index][col_index] == "B":
        return True
    return False


def check_for_invalid_indexes(r_index, c_index, constant_size):
    if 0 <= r_index < constant_size and 0 <= c_index < constant_size:
        return True
    return False


def keep_track_of_whos_turn(current_turn):
    if not current_turn % 2 == 0:
        current_turn += 1
        return "first", current_turn
    else:
        current_turn += 1
        return "second", current_turn


def calculating_points(r_index, c_index, constant_size, board, player_points):
    left_value = int(board[r_index][0])
    top_value = int(board[0][c_index])
    right_value = int(board[r_index][constant_size - 1])
    down_value = int(board[constant_size - 1][c_index])
    sum_values = left_value + top_value + right_value + down_value
    if board[r_index][c_index] == "D":
        player_points -= sum_values * 2
        return player_points
    elif board[r_index][c_index] == "T":
        player_points -= sum_values * 3
        return player_points
    else:
        value = int(board[r_index][c_index])
        return player_points - value


players_names = input().split(", ")

dartboard = [input().split() for el in range(BOARD_SIZE)]

first_player_points = 501
second_player_points = 501

first_player_turns = 0
second_player_turns = 0

value_for_player_turn = 1

while first_player_points > 0 and second_player_points > 0:
    current_player, value_for_player_turn = keep_track_of_whos_turn(value_for_player_turn)
    # print(current_player)
    # print(value_for_player_turn)
    current_shot = re.findall(r"\d", input())
    row_index = int(current_shot[0])
    column_index = int(current_shot[1])
    if current_player == "first":
        first_player_turns += 1
        if check_for_invalid_indexes(row_index, column_index, BOARD_SIZE):
            if check_for_b(row_index, column_index, dartboard):
                first_player_points = 0
            else:
                first_player_points = calculating_points(row_index, column_index, BOARD_SIZE, dartboard,
                                                         first_player_points)

    elif current_player == "second":
        second_player_turns += 1
        if check_for_invalid_indexes(row_index, column_index, BOARD_SIZE):
            if check_for_b(row_index, column_index, dartboard):
                second_player_points = 0
            else:
                second_player_points = calculating_points(row_index, column_index, BOARD_SIZE, dartboard,
                                                          second_player_points)


if first_player_points <= 0:
    print_result(players_names[0], first_player_turns)
elif second_player_points <= 0:
    print_result(players_names[1], first_player_turns)

# print(keep_track_of_whos_turn(value_for_player_turn))
# print(players_names)
# print(dartboard)
