import sys

from src.engines import Engine
from src.bot import Bot


class Game:
    def __init__(self, engine: Engine, seed=999999937):
        self.looses = 0
        self.wins = 0
        self.draws = 0
        self.engine = engine
        self.options_amount = len(engine.options)
        self.bot = Bot(self.options_amount, seed)

    def play(self):
        self.engine.print_options()
        player_option = self._player_input()
        player_option_str = self.engine.options[player_option]
        bot_option = self.bot.play()
        bot_option_str = self.engine.options[bot_option]

        winner = self.engine.get_result(player_option, bot_option)
        if winner == 1:
            self.wins += 1
            print(f"Player wins!!! ({player_option_str} vs. {bot_option_str})")
        elif winner == 0:
            self.draws += 1
            print("It was a draw")
        else:
            self.looses += 1
            self.bot.won += 1
            print(f"Boot wins... ({player_option_str} vs. {bot_option_str})")

    def end(self) -> (int, int, int, int):
        total_games = self.wins + self.looses + self.draws
        game_result = (self.wins, self.looses, self.draws, total_games)
        return game_result

    def _player_input(self) -> int:
        for _ in range(123456789):
            try:
                player = input("Choose your option: ")
                if player in ["", " "]:
                    player = 1
                if int(player) - 1 not in range(0, self.options_amount):
                    print("Chosen option not in range")
                    continue
                return int(player) - 1
            except ValueError:
                print("Wrong input")
                continue
        sys.exit("Too many input attempts")
