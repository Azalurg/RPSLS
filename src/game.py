from src.engines import Engine
from src.bot import Bot


class Game:
    def __init__(self, engine: Engine, seed=999999937):
        self.looses = 0
        self.wins = 0
        self.draws = 0
        self.engine = engine
        self.bot = Bot(len(engine.options), seed)

    def play(self):
        self.engine.print_options()
        player_option = int(input("Choose your option: ")) - 1
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
            print(f"Boot wins... ({player_option_str} vs. {bot_option_str})")

    def end(self) -> (int, int, int, int):
        total_games = self.wins + self.looses + self.draws
        game_result = (self.wins, self.looses, self.draws, total_games)
        return game_result
