from beginning import initial_tiles_deal, introduction, coin_toss
from player_turn import player_turn
from computer_turn import computer_turn
from collections import deque
from helper_functions import checking_who_won


dominoes_pool = {
    '00': [0, 0], '01': [0, 1], '02': [0, 2], '03': [0, 3], '04': [0, 4], '05': [0, 5], '06': [0, 6],
    '11': [1, 1], '12': [1, 2], '13': [1, 3], '14': [1, 4], '15': [1, 5], '16': [1, 6], '22': [2, 2],
    '23': [2, 3], '24': [2, 4], '25': [2, 5], '26': [2, 6], '33': [3, 3], '34': [3, 4], '35': [3, 5],
    '36': [3, 6], '44': [4, 4], '45': [4, 5], '46': [4, 6], '55': [5, 5], '56': [5, 6], '66': [6, 6],
}

board = deque()

# introduction()
player_tiles, computer_tiles = initial_tiles_deal(dominoes_pool)

print("\nThese are your initial tiles:", list(player_tiles.values()))

turn = deque(coin_toss())


def play_game():
    skip_turn = [0]

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


play_game()

