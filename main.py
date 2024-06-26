"""Main game loop"""
import os

from src.engines import SimpleEngine, AdvanceEngine
from src.game import Game


def main_loop():
    simple_game = Game(SimpleEngine())
    advance_game = Game(AdvanceEngine())

    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome to Rock Paper Scissors (Lizard Spock)")

    for _ in range(123456789):
        print("Choose game mode: *1. RPS*; 2. RPSLS; 0. Exit")
        decision = input("Decision: ")
        if decision == "0":
            break
        if decision in ["1", "", " "]:
            simple_game.play()
        elif decision == "2":
            advance_game.play()
        else:
            print("Wrong input !!! Expected '1', '2', or '0'")
            continue

        next_game = input("Want to try again? (Y/n): ")
        os.system("cls" if os.name == "nt" else "clear")
        if next_game.lower() not in ["", " ", "y", "yes"]:
            break

    print("Results RPS:")
    sgr = simple_game.end()  # simple game results
    print("w\tl\td\ttotal")
    print(f"{sgr[0]}\t{sgr[1]}\t{sgr[2]}\t{sgr[3]}\t")

    print("Results RPSLS")
    agr = advance_game.end()  # advance game results
    print("w\tl\td\ttotal")
    print(f"{agr[0]}\t{agr[1]}\t{agr[2]}\t{agr[3]}\t\n")

    if sgr[0] + agr[0] > sgr[1] + agr[1]:
        print("Congratulations! You win!")
    elif sgr[0] + agr[0] < sgr[1] + agr[1]:
        print("Unfortunately Bot wins :-(")
    else:
        print("What a game, but it is a draw...")
    return 0


if __name__ == "__main__":
    main_loop()
