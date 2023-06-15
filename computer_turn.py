import random as rd
from helper_functions import board_ends


def computer_turn(computer_tiles, board, dominoes_pool, skip_turn):
    computer_tiles_numbers = set(num for sublist in computer_tiles.values() for num in sublist)
    board_end_numbers = board_ends(board) if board else None

    if not board or any(num in board_end_numbers for num in computer_tiles_numbers):
        computer_selection = computer_selecting_tile(computer_tiles, board)
        tile_placement(computer_selection, board, computer_tiles)
        computer_tile = computer_tiles[computer_selection]
        print(f"Computer placed tile {computer_tile}")


    else:
        if not dominoes_pool:
            print("The dominoes pool is empty. No tiles can be drawn.")
            skip_turn[0] += 1

        print("\nComputer doesn't have any suitable tile to place. Drawing a tile...")
        new_tile_key, new_tile_value = rd.choice(list(dominoes_pool.items()))
        del dominoes_pool[new_tile_key]
        computer_tiles[new_tile_key] = new_tile_value


def tile_placement(computer_selection, board, computer_tiles):

    if board:
        board_begin, board_end = board_ends(board)
        computer_digits = [int(digit) for digit in str(computer_selection)]

        if has_multiple_placement_options(computer_digits, board_begin, board_end):
            handle_multiple_placement_options(computer_selection, board, computer_tiles, board_begin, board_end)
        else:
            handle_single_placement_option(computer_selection, board, computer_tiles, board_begin, board_end, computer_digits)
    else:
        handle_empty_board_placement(computer_selection, board, computer_tiles)


def has_multiple_placement_options(computer_digits, board_begin, board_end):
    return any([
        computer_digits[0] == board_end == board_begin,
        computer_digits[1] == board_end == board_begin,
        (computer_digits[0] == board_begin and computer_digits[1] == board_end),
        (computer_digits[0] == board_end and computer_digits[1] == board_begin)
    ])


def handle_multiple_placement_options(computer_selection, board, computer_tiles, board_begin, board_end):
    print("Computer has a choice to place the selected tile in the beginning or the end of the board")
    if rd.choice([True, False]):
        place_tile_at_beginning(computer_selection, board, computer_tiles, board_begin)
    else:
        place_tile_at_end(computer_selection, board, computer_tiles, board_end)

    del computer_tiles[computer_selection]


def handle_single_placement_option(player_selection, board, computer_tiles, board_begin, board_end, computer_digits):
    print("Computer has only one possible place for his tile!")
    if board_begin in computer_digits:
        place_tile_at_beginning(player_selection, board, computer_tiles, board_begin)
    else:
        place_tile_at_end(player_selection, board, computer_tiles, board_end)


def handle_empty_board_placement(computer_selection, board, player_tiles):
    print("Board is empty, so computer places his selected tile in the middle!")
    place_tile_at_end(computer_selection, board, player_tiles, None)


def place_tile_at_beginning(computer_selection, board, computer_tiles, board_begin):
    player_tile = get_computer_tile(computer_selection, computer_tiles)
    if player_tile[0] == board_begin:
        player_tile = [player_tile[1], player_tile[0]]
    board.appendleft(player_tile)


def place_tile_at_end(computer_selection, board, computer_tiles, board_end):
    computer_tile = get_computer_tile(computer_selection, computer_tiles)
    if computer_tile[1] == board_end:
        computer_tile = [computer_tile[1], computer_tile[0]]
    board.append(computer_tile)


def get_computer_tile(computer_selection, computer_tiles):
    return computer_tiles[computer_selection]


def computer_selecting_tile(computer_tiles, board):
    counting_tiles = {}

    if board:
        board_begin, board_end = board_ends(board)

        relevant_tiles = [tile for tile in computer_tiles if
                          any(digit == board_end or digit == board_begin for digit in computer_tiles[tile])]
    else:
        relevant_tiles = list(computer_tiles.keys())

    for tile in relevant_tiles:
        digits = set(computer_tiles[tile])
        count = 0

        for other_tile in relevant_tiles:
            if other_tile != tile:
                other_digits = set(computer_tiles[other_tile])
                common_digits = digits.intersection(other_digits)
                count += len(common_digits)

        counting_tiles[tile] = count

    sorted_counting_tiles = sorted(counting_tiles, key=counting_tiles.get, reverse=True)

    highest_count = counting_tiles[sorted_counting_tiles[0]]

    tiles_with_highest_count = [tile for tile in sorted_counting_tiles if counting_tiles[tile] == highest_count]

    return rd.choice(tiles_with_highest_count)