import random as rd
from helper_functions import board_ends, print_board


def player_turn(player_tiles, board, dominoes_pool, skip_turn):
    player_tiles_numbers = set(num for sublist in player_tiles.values() for num in sublist)
    board_end_numbers = board_ends(board) if board else None

    while True:
        print(f"\nThese are your tiles: {list(player_tiles.values())}")
        print_board(board)

        if not board or any(num in board_end_numbers for num in player_tiles_numbers):
            player_selection = input("Please select a tile which you wish to place: ")

            if player_selection in player_tiles:
                player_digits = [int(digit) for digit in player_selection]

                if not board or any(player_digit in board_end_numbers for player_digit in player_digits):
                    tile_placement(player_selection, board, player_tiles)
                    skip_turn[0] = 0
                    break

                print("You can't place that tile, but you have other tile(s) that you can place. Choose again!")
            else:
                print("You have to type the value of the tile, for example for tile [0, 1] you have to enter '01'!")
        else:
            if not dominoes_pool:
                print("The dominoes pool is empty. No tiles can be drawn.")
                skip_turn[0] += 1
                break

            print("\nYou don't have any suitable tile to place. Drawing a tile...")
            new_tile_key, new_tile_value = rd.choice(list(dominoes_pool.items()))
            del dominoes_pool[new_tile_key]
            player_tiles[new_tile_key] = new_tile_value
            print(f"Your new tile is {new_tile_value}")
            break


def tile_placement(player_selection, board, player_tiles):
    if board:
        board_begin, board_end = board_ends(board)
        player_digits = [int(digit) for digit in str(player_selection)]

        if has_multiple_placement_options(player_digits, board_begin, board_end):
            handle_multiple_placement_options(player_selection, board, player_tiles, board_begin, board_end)
        else:
            handle_single_placement_option(player_selection, board, player_tiles, board_begin, board_end, player_digits)
    else:
        handle_empty_board_placement(player_selection, board, player_tiles)


def has_multiple_placement_options(player_digits, board_begin, board_end):
    return any([
        player_digits[0] == board_end == board_begin,
        player_digits[1] == board_end == board_begin,
        (player_digits[0] == board_begin and player_digits[1] == board_end),
        (player_digits[0] == board_end and player_digits[1] == board_begin)
    ])


def handle_multiple_placement_options(player_selection, board, player_tiles, board_begin, board_end):
    print("You have a choice to place your tile in the beginning or end of the board")
    while True:
        which_end = input("Please choose (L)eft end or (R)ight end: ").lower()
        if which_end in ["l", "left"]:
            place_tile_at_beginning(player_selection, board, player_tiles, board_begin)
            break
        elif which_end in ["r", "right"]:
            place_tile_at_end(player_selection, board, player_tiles, board_end)
            break
        else:
            print("That's not a valid choice! Please type l for Left or r for Right")


def handle_single_placement_option(player_selection, board, player_tiles, board_begin, board_end, player_digits):
    print("You have only one possible place for your tile!")
    if board_begin in player_digits:
        place_tile_at_beginning(player_selection, board, player_tiles, board_begin)
    else:
        place_tile_at_end(player_selection, board, player_tiles, board_end)


def handle_empty_board_placement(player_selection, board, player_tiles):
    print("Board is empty, so you place your selected tile in the middle!")
    place_tile_at_end(player_selection, board, player_tiles, None)


def place_tile_at_beginning(player_selection, board, player_tiles, board_begin):
    player_tile = get_player_tile(player_selection, player_tiles)
    if player_tile[0] == board_begin:
        player_tile = [player_tile[1], player_tile[0]]
    board.appendleft(player_tile)
    del player_tiles[player_selection]


def place_tile_at_end(player_selection, board, player_tiles, board_end):
    player_tile = get_player_tile(player_selection, player_tiles)
    if player_tile[1] == board_end:
        player_tile = [player_tile[1], player_tile[0]]
    board.append(player_tile)
    del player_tiles[player_selection]


def get_player_tile(player_selection, player_tiles):
    return player_tiles[player_selection]


