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


def checking_who_won(player_tiles, computer_tiles):
    player_tiles_count = len(player_tiles)
    computer_tiles_count = len(computer_tiles)
    if computer_tiles_count == 0:
        print("\nComputer has no more tiles. You lost!")
    elif player_tiles_count == 0:
        print("\nYou have no more tiles. Computer lost!")
    elif player_tiles_count > computer_tiles_count:
        print(f"Tiles remaining - Player: {player_tiles_count}, Computer: {computer_tiles_count}. You lost!")
    elif computer_tiles_count > player_tiles_count:
        print(f"Tiles remaining - Player: {player_tiles_count}, Computer: {computer_tiles_count}. You won!")
    else:
        print(f"Both player and computer has {player_tiles_count} tiles remaining. Game ends in a draw!")