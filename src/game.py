import os
from random import randint
from src.engines import SimpleEngine, AdvanceEngine


class Game:
    def __init__(self):
        self.weapon = {
            0: "Rock",
            1: "Paper",
            2: "Scissors",
            3: "Lizard",
            4: "Spock"
        }
        self.looses = 0
        self.wins = 0
        self.draws = 0
        self.simple = SimpleEngine()
        self.advance = AdvanceEngine()

    def start(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        print("Welcome to Rock Paper Scissors (Lizard Spock)")
        while True:
            print("0. Break; 1. Rock; 2. Paper; 3. Scissors")
            decision = int(input("Decision: "))
            if decision <= 0:
                break
            decision -= 1
            bot = randint(0, 2)
            print(
                "You: {};\tBot: {}".format(
                    self.weapon.get(decision), self.weapon.get(bot)
                )
            )
            winner = self.simple.get_result(decision, bot)
            if winner == 1:
                print("Win")
            elif winner == 0:
                print("Draw")
            else:
                print("Loos")
            os.system("cls" if os.name == "nt" else "clear")
        print("The End")
