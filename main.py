import os

from src.engines import SimpleEngine, AdvanceEngine
from src.game import Game

if __name__ == "__main__":
    simple_game = Game(SimpleEngine())
    advance_game = Game(AdvanceEngine())
    i = 0

    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome to Rock Paper Scissors (Lizard Spock)")

    while True or i < 123456789:
        print("Choose game mode: 1. RPS; 2. RPSLS; 0. Exit")
        decision = input("Decision: ")
        if decision == "0":
            break
        elif decision == "1":
            simple_game.play()
        elif decision == "2":
            advance_game.play()
        else:
            print("Wrong input !!! Expected '1', '2', or '0'")
            continue

        next_game = input("Want to try again? (Y/n): ")
        if next_game.lower() not in ["", " ", "y", "yes"]:
            break
