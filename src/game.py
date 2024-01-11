import os
from random import randint
class Game:
    def __init__(self):
        self.simple = {0: "Rock", 1: "Paper", 2: "Scissors"}
        self.matrix = [[0, -1, 1],
                       [1, 0, -1],
                       [-1, 1, 0]]
    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to Rock Paper Scissors (Lizard Spock)")
        while True:
            print("0. Break; 1. Rock; 2. Paper; 3. Scissors")
            decision = int(input("Decision: "))
            if decision <= 0:
                break
            decision -= 1
            bot = randint(0, 2)
            print("You: {};\tBot: {}".format(self.simple.get(decision), self.simple.get(bot)))
            winner = self.matrix[decision][bot]
            if winner == 1:
                print("Win")
            elif winner == 0:
                print("Draw")
            else:
                print("Loos")
            os.system('cls' if os.name == 'nt' else 'clear')
        print("The End")
