def board_ends(board):
    first_end = board[0][0]
    second_end = board[-1][1]
    return first_end, second_end


def print_board(board):
    if len(board) == 0:
        print("The board is still empty!")
    else:
        print("This is how the board looks like now:", end=" ")
        print(*board, sep=" ")