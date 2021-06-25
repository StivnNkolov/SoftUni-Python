from math import ceil


def check_for_valid_indexes(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False

def up_movement(board, player_row, player_col):
    up_move = (-1, 0)
    next_position_row = player_row + up_move[0]
    next_position_col = player_col + up_move[1]


input_number_for_board_size = int(input())

game_board = []
player_location = ()
for row in range(input_number_for_board_size):
    current_row = input().split()
    game_board.append(current_row)
    if "P" in current_row:
        player_location = row, current_row.index("P")

player_path = []
collected_coins = 0

while collected_coins < 100:
    current_player_row, current_player_col = player_location
    input_player_movement_command = input()
    if input_player_movement_command == "up":
        up_move = (-1, 0)
        next_position_row = current_player_row + up_move[0]
        next_position_col = current_player_col + up_move[1]
        if check_for_valid_indexes(next_position_row, next_position_col, input_number_for_board_size):
            if game_board[next_position_row][next_position_col] == "X":
                collected_coins = collected_coins // 2
                break
            else:
                collected_coins += int(game_board[next_position_row][next_position_col])
                player_location = next_position_row, next_position_col
                player_path.append([next_position_row, next_position_col])
        else:
            collected_coins = collected_coins // 2
            break
    elif input_player_movement_command == "down":
        down_move = (+1, 0)
        next_position_row = current_player_row + down_move[0]
        next_position_col = current_player_col + down_move[1]
        if check_for_valid_indexes(next_position_row, next_position_col, input_number_for_board_size):
            if game_board[next_position_row][next_position_col] == "X":
                collected_coins = collected_coins // 2
                break
            else:
                collected_coins += int(game_board[next_position_row][next_position_col])
                player_location = next_position_row, next_position_col
                player_path.append([next_position_row, next_position_col])
        else:
            collected_coins = collected_coins // 2
            break

    elif input_player_movement_command == "left":
        left_move = (0, -1)
        next_position_row = current_player_row + left_move[0]
        next_position_col = current_player_col + left_move[1]
        if check_for_valid_indexes(next_position_row, next_position_col, input_number_for_board_size):
            if game_board[next_position_row][next_position_col] == "X":
                collected_coins = collected_coins // 2
                break
            else:
                collected_coins += int(game_board[next_position_row][next_position_col])
                player_location = next_position_row, next_position_col
                player_path.append([next_position_row, next_position_col])
        else:
            collected_coins = collected_coins // 2
            break
    elif input_player_movement_command == "right":
        right_move = (0, +1)
        next_position_row = current_player_row + right_move[0]
        next_position_col = current_player_col + right_move[1]
        if check_for_valid_indexes(next_position_row, next_position_col, input_number_for_board_size):
            if game_board[next_position_row][next_position_col] == "X":
                collected_coins = collected_coins // 2
                break
            else:
                collected_coins += int(game_board[next_position_row][next_position_col])
                player_location = next_position_row, next_position_col
                player_path.append([next_position_row, next_position_col])
        else:
            collected_coins = collected_coins // 2
            break
    else:
        continue

if collected_coins >= 100:
    print(f"You won! You've collected {ceil(collected_coins)} coins.")
else:
    print(f"Game over! You've collected {ceil(collected_coins)} coins.")
print("Your path: ")
print(*player_path, sep="\n")
