import sys


class Engine:
    def __init__(self, conditions, options):
        self.conditions = conditions
        self.options = options

        if len(self.conditions) != len(self.options):
            sys.exit("Wrong game engine - conditions don't match options")

    def get_result(self, player: int, bot: int) -> int:
        return self.conditions[player][bot]

    def print_options(self):
        for i, option in enumerate(self.options):
            if i == 0:
                print(f"*{i+1}. {option}*", end="; ")
            else:
                print(f"{i+1}. {option}", end="; ")
        print("")


class SimpleEngine(Engine):
    def __init__(self):
        conditions = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
        options = ["Rock", "Paper", "Scissors"]
        super().__init__(conditions, options)


class AdvanceEngine(Engine):
    def __init__(self):
        conditions = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0],
        ]
        options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

        super().__init__(conditions, options)
