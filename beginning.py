import random as rd
import error_messages


def introduction():
    print("Welcome to the 'Dominoes' game.")
    print("The goal of the game is to beat the opponent by placing all your tiles, before he is able to do the same.")
    while True:
        choice = input("Do you want to read the full rules: (Y)es or (N)o: ").lower()
        if choice in ["y", "yes"]:
            print("There are a total of 28 tiles in Domino, with two sides and numbers from 0 do 6 on each side.")
            print("Tiles are represented like this: [0, 2] which means 0 on one side and 2 on the other side.")
            print("Each player randomly receives 7 tiles and the other 14 tiles go into a domino pool.")
            print("The board looks like this: [0, 1] [1, 5] [5, 2] etc. Tiles can be joined only if they share the same number.")
            print(" Tiles can be rotated so [1, 5] can be placed on a board [2, 5] and the result is [2, 5] [5, 1].")
            print("If a player has no suitable tile in hand he must draw randomly one tile from the dominoes pool.")
            print("The winner is the first player who has no tiles in his hand.")
            print("There might be a scenario where both players can't play a tile and there are no more tiles to draw.")
            print("In this case the winner is the player who has lower number of tiles in his hand.")
            print("A coin toss decides who will start first, so let the game begins!!!")
            break
        elif choice in ["n", "no"]:
            break
        else:
            error_messages.error_not_valid()
            continue


def initial_tiles_deal(dominoes_pool):

    player_tiles_list = rd.sample(list(dominoes_pool.keys()), 7)
    player_tiles = {tile: dominoes_pool[tile] for tile in player_tiles_list}

    for tile in player_tiles:
        del dominoes_pool[tile]

    computer_tiles_list = rd.sample(list(dominoes_pool.keys()), 7)
    computer_tiles = {tile: dominoes_pool[tile] for tile in computer_tiles_list}

    for tile in computer_tiles:
        del dominoes_pool[tile]

    return player_tiles, computer_tiles


def coin_toss():
    print("\nIn order to decide who starts first, let's throw a coin.")
    while True:
        player_choice = input("Please select - (H)ead or (T)ail: ").lower()
        if player_choice not in ["head", "tail", "h", "t"]:
            error_messages.error_head_tail_only()
        else:
            break

    toss_result = rd.choice(range(1, 3))

    if toss_result == 1:
        print("The coin toss result is 'Head'!")
        if player_choice in ["head", "h"]:
            print("You start first!")
            return "Player", "Computer"
    else:
        print("The coin toss result is 'Tail'!")
        if player_choice in ["tail", "t"]:
            print("You start first!")
            return "Player", "Computer"

    print("Computer starts first!")
    return "Computer", "Player"
