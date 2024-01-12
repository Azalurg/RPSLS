class Bot:
    def __init__(self, options: int = 3, seed: int = 999983):
        self.games_played = 0
        self.game_won = 0
        self.seed = seed
        self.options = options

    def play(self) -> int:
        self.games_played += 1
        return self.get_seed() % self.options

    def get_seed(self):
        self.seed = (self.seed * self.games_played + self.game_won) % 9999991
        return self.seed
