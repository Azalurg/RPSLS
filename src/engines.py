import sys
from enum import Enum


class Options(Enum):
    Rock = 0
    Paper = 1
    Scissors = 2


class ExtendedOptions(Enum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


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
        return self.options(option).name


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
