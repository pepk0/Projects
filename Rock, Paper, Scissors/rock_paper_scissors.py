import colorama
import time
from colorama import Fore
from prettytable import PrettyTable
from random import randint


def get_user_choice(prompt: str) -> int:
    """"prompts the user for specific input = int in range 1-4"""
    while True:
        try:
            choice = int(input(prompt))
            if choice in range(1, 5):
                return choice
            else:
                raise ValueError
        except ValueError:
            print(Fore.RED + "\ninvalid integer number! (1-4)")


def print_winner(com_choice: int, play_choice: int, score: list,
                 choices: dict) -> PrettyTable:
    """"gets the formats the output in a table, displays score"""
    table = PrettyTable()
    com_choice = choices[com_choice]
    play_choice = choices[play_choice]
    result = f"{score[0]} - {score[1]}"

    table.field_names = ["You", "Computer", "Score"]
    table.add_row([play_choice, com_choice, result])

    return table


def get_winner(computer: int, player: int) -> str:
    """compares the results from the computer player"""
    winner = ""
    if computer == player:
        winner = "Draw"
    elif computer == 3 and player == 1:
        winner = "You"
    elif computer == 3 and player == 2:
        winner = "Computer"
    elif computer == 2 and player == 1:
        winner = "Computer"
    elif computer == 2 and player == 3:
        winner = "You"
    elif computer == 1 and player == 3:
        winner = "Computer"
    elif computer == 1 and player == 2:
        winner = "You"

    return winner


def main():
    # makes the color default to normal after the print
    colorama.init(autoreset=True)
    # initializing pretty table

    prompt = ("\n[1]-Paper, "
              "[2]-Scissors, [3]-Rock, [4]-Quit - Please, enter your choice: ")
    score = [0, 0]
    choices = {1: "Paper", 2: "Scissors", 3: "Rock"}

    while True:

        computer_choice = randint(1, 3)
        player_choice = get_user_choice(prompt)

        if player_choice == 4:
            print(Fore.CYAN + "\nThanks for playing!\n")
            break

        print("\nRock, Paper, Scissors 1.. 2.. 3..")
        # stops the program for 0.6 sec to se the illusion of choosing
        time.sleep(0.6)  
        winner = get_winner(computer_choice, player_choice)

        if winner == "You":
            score[0] += 1
            print(Fore.GREEN + f"\n\tYou win!")
        elif winner == "Computer":
            print(Fore.RED + f"\n\tYou lose!")
            score[1] += 1
        else:
            print(Fore.CYAN + f"\n\tDraw!")

        print(print_winner(computer_choice, player_choice, score, choices))


if __name__ == "__main__":
    main()
