import sys
from enum import Enum


class Options(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class ExtendedOptions(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    LIZARD = 3
    SPOCK = 4


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
                print(f"*{i+1}. {option.name}*", end="; ")
            else:
                print(f"{i+1}. {option.name}", end="; ")
        print("")

    def get_string(self, option: int) -> str:
        return str(self.options(option).name).capitalize()


class SimpleEngine(Engine):
    def __init__(self):
        conditions = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
        super().__init__(conditions, Options)


class AdvanceEngine(Engine):
    def __init__(self):
        conditions = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0],
        ]

        super().__init__(conditions, ExtendedOptions)
