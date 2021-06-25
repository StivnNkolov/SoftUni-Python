def create_board_and_find_s(number):
    board = []
    s_position = ()
    for row in range(number):
        current_row = [el for el in input()]
        board.append(current_row)
        if "S" in current_row:
            s_position = (row, current_row.index("S"))
    return board, s_position


def find_teleport_place(board):
    b_position = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "B":
                b_position.append((row, col))
    return b_position


def check_if_index_is_valid(tuple_with_indexes, number):
    first_index = tuple_with_indexes[0]
    second_index = tuple_with_indexes[1]
    if 0 <= first_index < number and 0 <= second_index < number:
        return True
    return False


def if_next_move_is_b(next_move_indexes, tele_positions, board, s_position):
    next_move_index_1 = next_move_indexes[0]
    next_move_index_2 = next_move_indexes[1]
    s_curr_position_index_1 = s_position[0]
    s_curr_position_index_2 = s_position[1]
    tele_positions.pop(tele_positions.index(next_move_indexes))
    board[next_move_index_1][next_move_index_2] = "."
    board[tele_positions[0][0]][tele_positions[0][1]] = "S"
    board[s_curr_position_index_1][s_curr_position_index_2] = "."
    s_position = (tele_positions[0][0], tele_positions[0][1])
    return board, s_position, tele_positions


def if_next_move_is_empty_move(board, next_move_indexes, s_position):
    board[next_move_indexes[0]][next_move_indexes[1]] = "S"
    snake_board[s_position[0]][s_position[1]] = "."
    s_position = (next_move_indexes[0], next_move_indexes[1])
    return board, s_position


def if_next_move_is_food(board, eaten_food, next_move_indexes, s_position):
    eaten_food += 1
    board[s_position[0]][s_position[1]] = "."
    board[next_move_indexes[0]][next_move_indexes[1]] = "S"
    s_position = (next_move_indexes[0], next_move_indexes[1])
    return board, eaten_food, s_position


def output_when_leaving_the_board(board, s_position):
    board[s_position[0]][s_position[1]] = "."
    print("Game over!")
    return board


input_size = int(input())

snake_board, snake_position_on_board = create_board_and_find_s(input_size)
teleports_positions = find_teleport_place(snake_board)
food_eaten = 0

while not food_eaten == 10:
    input_move_command = input()
    snake_row, snake_column = snake_position_on_board

    if input_move_command == "up":
        up_move = (snake_row - 1, snake_column)
        if check_if_index_is_valid(up_move, len(snake_board)):
            if snake_board[up_move[0]][up_move[1]] == "B":

                snake_board, snake_position_on_board, teleports_positions = if_next_move_is_b(up_move,
                                                                                              teleports_positions,
                                                                                              snake_board,
                                                                                              snake_position_on_board)
            elif snake_board[up_move[0]][up_move[1]] == "-":
                snake_board, snake_position_on_board = if_next_move_is_empty_move(snake_board, up_move,
                                                                                  snake_position_on_board)
            elif snake_board[up_move[0]][up_move[1]] == "*":
                snake_board, food_eaten, snake_position_on_board = if_next_move_is_food(snake_board, food_eaten,
                                                                                        up_move,
                                                                                        snake_position_on_board)

        else:
            snake_board = output_when_leaving_the_board(snake_board, snake_position_on_board)
            break
    elif input_move_command == "down":
        down_move = (snake_row + 1, snake_column)
        if check_if_index_is_valid(down_move, len(snake_board)):
            if snake_board[down_move[0]][down_move[1]] == "B":
                snake_board, snake_position_on_board, teleports_positions = if_next_move_is_b(down_move,
                                                                                              teleports_positions,
                                                                                              snake_board,
                                                                                              snake_position_on_board)
            elif snake_board[down_move[0]][down_move[1]] == "-":
                snake_board, snake_position_on_board = if_next_move_is_empty_move(snake_board, down_move,
                                                                                  snake_position_on_board)
            elif snake_board[down_move[0]][down_move[1]] == "*":
                snake_board, food_eaten, snake_position_on_board = if_next_move_is_food(snake_board, food_eaten,
                                                                                        down_move,
                                                                                        snake_position_on_board)
        else:
            snake_board = output_when_leaving_the_board(snake_board, snake_position_on_board)
            break
    elif input_move_command == "left":
        left_move = (snake_row, snake_column - 1)
        if check_if_index_is_valid(left_move, len(snake_board)):
            if snake_board[left_move[0]][left_move[1]] == "B":
                snake_board, snake_position_on_board, teleports_positions = if_next_move_is_b(left_move,
                                                                                              teleports_positions,
                                                                                              snake_board,
                                                                                              snake_position_on_board)
            elif snake_board[left_move[0]][left_move[1]] == "-":
                snake_board, snake_position_on_board = if_next_move_is_empty_move(snake_board, left_move,
                                                                                  snake_position_on_board)
            elif snake_board[left_move[0]][left_move[1]] == "*":
                snake_board, food_eaten, snake_position_on_board = if_next_move_is_food(snake_board, food_eaten,
                                                                                        left_move,
                                                                                        snake_position_on_board)
        else:
            snake_board = output_when_leaving_the_board(snake_board, snake_position_on_board)
            break
    elif input_move_command == "right":
        right_move = (snake_row, snake_column + 1)
        if check_if_index_is_valid(right_move, len(snake_board)):
            if snake_board[right_move[0]][right_move[1]] == "B":
                snake_board, snake_position_on_board, teleports_positions = if_next_move_is_b(right_move,
                                                                                              teleports_positions,
                                                                                              snake_board,
                                                                                              snake_position_on_board)
            elif snake_board[right_move[0]][right_move[1]] == "-":
                snake_board, snake_position_on_board = if_next_move_is_empty_move(snake_board, right_move,
                                                                                  snake_position_on_board)
            elif snake_board[right_move[0]][right_move[1]] == "*":
                snake_board, food_eaten, snake_position_on_board = if_next_move_is_food(snake_board, food_eaten,
                                                                                        right_move,
                                                                                        snake_position_on_board)
        else:
            snake_board = output_when_leaving_the_board(snake_board, snake_position_on_board)
            break

if food_eaten == 10:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_eaten}")
[print(*el, sep="") for el in snake_board]
