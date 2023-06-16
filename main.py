from beginning import initial_tiles_deal, introduction, coin_toss
from player_turn import player_turn
from computer_turn import computer_turn
from collections import deque
from helper_functions import checking_who_won, print_final_stats

dominoes_pool = {str(i) + str(j): [i, j] for i in range(7) for j in range(i, 7)}
player_tiles, computer_tiles = initial_tiles_deal(dominoes_pool)
board = deque()
skip_turn = [0]

introduction()
turn = deque(coin_toss())


def play_game():
    while player_tiles and computer_tiles:
        if turn[0] == "Player":
            player_turn(player_tiles, board, dominoes_pool, skip_turn)
            turn.rotate()
        else:
            computer_turn(computer_tiles, board, dominoes_pool, skip_turn)
            print(f"Computer has {len(computer_tiles)} tiles in his hand!")
            turn.rotate()

        if skip_turn[0] == 2:
            print("\nBoth players can't draw anymore. Counting the remaining tiles to determine winner ...")
            break

    checking_who_won(player_tiles, computer_tiles)
    print_final_stats(player_tiles, computer_tiles, dominoes_pool)


play_game()

