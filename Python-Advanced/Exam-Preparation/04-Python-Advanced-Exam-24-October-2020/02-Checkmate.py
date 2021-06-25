def finding_queens(delt, board, k_r, k_c):
    for i in range(len(board)):
        current_row = k_r + delt[0]
        current_col = k_c + delt[1]
        if 0 <= current_row < len(board) and 0 <= current_col < len(board):
            current_place = board[current_row][current_col]
            if current_place == "Q":
                return [current_row, current_col]
            else:
                k_r = current_row
                k_c = current_col


chess_board = []
king_location = ()

for row in range(8):
    curr_row = input().split()
    chess_board.append(curr_row)
    if "K" in curr_row:
        king_location = row, curr_row.index("K")

queens_locations = []
king_row = king_location[0]
king_col = king_location[1]

deltas = [(0, -1), (-1, -1), (-1, 0), (-1, +1), (0, +1), (+1, +1), (+1, 0), (+1, -1)]

for delta in deltas:
    queen = finding_queens(delta, chess_board, king_row, king_col)
    if queen:
        queens_locations.append(queen)

if not queens_locations:
    print("The king is safe!")
else:
    [print(el) for el in queens_locations]
