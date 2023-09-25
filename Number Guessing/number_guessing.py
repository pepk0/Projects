from random import choice
import time
import colorama
from colorama import Fore


def get_level(prompt: str) -> int:
    while True:
        try:
            level = int(input(prompt))
            if level in range(0, 4):
                return level
            else:
                raise ValueError
        except ValueError:
            print("Invalid integer (0, 1, 2, 3)")


def take_guess(prompt: str) -> int:
    while True:
        try:
            guess = int(input(prompt))
            return guess
        except ValueError:
            print("invalid integer")


def main():

    colorama.init(autoreset=True)

    guesses = 0
    total_guesses = 5
    print(Fore.BLUE + "Welcome to Number Guesser!")
    levels = {1: range(1, 11), 2: range(1, 26), 3: range(1, 36)}
    level = get_level(
        Fore.BLUE + "Pick a difficulty level: [1] [2] [3] or [0] to quit: ")
    if level == 0:
        print(Fore.BLUE + "Thanks for playing!")
        return
    secret_number = choice(levels[level])
    print(Fore.CYAN + f"I am thinking of a number in the {levels[level]}")
    time.sleep(0.5)
    print(Fore.CYAN + "Done!")

    while guesses < total_guesses:
        player_guess = take_guess(Fore.CYAN + "Try to guess it: ")
        guesses += 1
        if secret_number > player_guess:
            print(Fore.RED + "Wrong, number is higher!")
        elif secret_number < player_guess:
            print(Fore.RED + "Wrong, number is lower!")
        else:
            print(Fore.GREEN + f"You got! it took you {guesses} guesses!")
            return
    else:
        print(Fore.RED + "Out of guesses!", Fore.BLUE + "Try again")
        print(Fore.BLUE + "Thanks for playing!")
        return


if __name__ == "__main__":
    main()
