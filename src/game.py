from src.engines import SimpleEngine, AdvanceEngine, Engine
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
            print("Win")
        elif winner == 0:
            self.draws += 1
            print("Draw")
        else:
            self.looses += 1
            print("Loos")
