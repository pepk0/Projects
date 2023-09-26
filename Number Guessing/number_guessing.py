from random import randint
import time
import colorama
from colorama import Fore


def get_level(prompt: str) -> int:
    """Gets a input from user > int in the range 0-3"""
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
    """Gets a valid int input"""
    while True:
        try:
            guess = int(input(prompt))
            return guess
        except ValueError:
            print("invalid integer")


def main():
    # auto clear color from terminal output after each line
    colorama.init(autoreset=True)

    guesses = 0
    total_guesses = 5
    levels = {1: (1, 10), 2: (1, 25), 3: (1, 35)}
    print(Fore.LIGHTYELLOW_EX + "Welcome to Number Guesser!")
    level = get_level(
        Fore.LIGHTYELLOW_EX + 
        "Pick a difficulty level: [1] [2] [3] or [0] to quit: ")

    if level == 0:
        print(Fore.LIGHTYELLOW_EX + "Thanks for playing!")
        return

    start, stop = levels[level]
    secret_number = randint(start, stop)
    print(Fore.CYAN +
          f"I am thinking of a number in the range of {start} - {stop}... ")
    # pauses the program for 0.5 sec to create the illusion of the computer
    # picking a number
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
        print(Fore.RED + "Out of guesses!", Fore.LIGHTYELLOW_EX + "Try again")
        print(Fore.LIGHTYELLOW_EX + "Thanks for playing!")
        return


if __name__ == "__main__":
    main()
