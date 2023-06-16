import colorama
from colorama import Fore

colorama.init(autoreset=True)


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
        print(Fore.RED + "\nComputer has no more tiles. You lost!")
    elif player_tiles_count == 0:
        print(Fore.LIGHTGREEN_EX + "\nYou have no more tiles. Computer lost!")
    elif player_tiles_count > computer_tiles_count:
        print(Fore.RED + f"Tiles remaining - Player: {player_tiles_count}, Computer: {computer_tiles_count}. You lost!")
    elif computer_tiles_count > player_tiles_count:
        print(Fore.LIGHTGREEN_EX + f"Tiles remaining - Player: {player_tiles_count}, Computer: {computer_tiles_count}. You won!")
    else:
        print(Fore.LIGHTBLUE_EX + f"Both player and computer has {player_tiles_count} tiles remaining. Game ends in a draw!")


def print_final_stats(player_tiles, computer_tiles, dominoes_pool):
    print()

    if len(player_tiles) > 0:
        print(f"You have {len(player_tiles)} tile(s) left: {' '.join(map(str, player_tiles.values()))}")

    if len(computer_tiles) > 0:
        print(f"Computer has {len(computer_tiles)} tile(s) left: {' '.join(map(str, computer_tiles.values()))}")

    if len(dominoes_pool) > 1:
        print(f"There are {len(dominoes_pool)} tiles left in the dominoes pool: {' '.join(map(str, dominoes_pool.values()))}")
    elif len(dominoes_pool) == 1:
        print(f"There is only 1 tile left in the dominoes pool: {' '.join(map(str, dominoes_pool.values()))}")
    else:
        print("There are no tiles left in the dominoes pool!")
