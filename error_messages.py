import colorama
from colorama import Fore

colorama.init(autoreset=True)


def error_wrong_tile():
    print(Fore.RED + "You can't place that tile, but you have other tile(s) that you can place. Choose again!")


def error_typo_tile():
    print(Fore.RED + "You have to type the value of the tile, for example for tile [0, 1] you have to enter '01'!")


def error_empty_pool():
    print(Fore.RED + "The dominoes pool is empty. No tiles can be drawn.")


def error_left_right_only():
    print(Fore.RED + "That's not a valid choice! Please type l for Left or r for Right")


def error_not_valid():
    print(Fore.RED + "Please select a valid option!")


def error_head_tail_only():
    print(Fore.RED + "You have to type 'head' or 'tail'!")