import random as rd


def introduction():
    print("Welcome to the 'Dominoes' game.")
    print("The goal of the game is to beat the opponent by placing all your tiles, before he is able to do the same.")
    while True:
        choice = input("Do you want to read the full rules: (Y)es or (N)o: ").lower()
        if choice in ["y", "yes"]:
            print("Full rules")
            break
        elif choice in ["n", "no"]:
            break
        else:
            print("Please select a valid option!")
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
        player_choice = input("Please select - Head or Tail: ").lower()
        if player_choice not in ["head", "tail"]:
            print("You have to type 'head' or 'tail'!")
        else:
            break

    toss_result = rd.choice(range(1, 3))

    if toss_result == 1:
        print("The coin toss result is 'Head'!")
        if player_choice == "head":
            print("You start first!")
            return "Player", "Computer"
    else:
        print("The coin toss result is 'Tail'!")
        if player_choice == "tail":
            print("You start first!")
            return "Player", "Computer"

    print("Computer starts first!")
    return "Computer", "Player"
