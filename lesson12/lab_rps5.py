import random
import sys
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            "\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
        print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉 You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉 You win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return "🐍 Python wins!"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print("\nGame count: " + str(game_count))
        print("Player wins: " + str(player_wins))
        print("Python wins: " + str(python_wins))
        print("Tie games: " + str(game_count - (player_wins + python_wins)))

        print("\nPlay again?")

        while True:
            playAgain = input("\nPlay again? \nY for Yes, or \nQ to quit: \n")
            if playAgain.lower() not in ["y", "q"]:
                print("You must enter Y or Q.")
                continue  # continue to prompt user for input inside this while loop until user enters "y" or "q"
            else:
                break  # break out of while loop if given "y" or "q"

        if playAgain.lower() == "y":
            return play_rps()
        else:
            print("\nThanks for playing!")
            playAgain = False
            sys.exit("Bye! 👋")

    return play_rps


play = rps()

play()
