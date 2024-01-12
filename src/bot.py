class Bot:
    def __init__(self, options: int = 3, seed: int = 999983):
        self.played = 0
        self.won = 0
        self.seed = seed
        self.options = options

    def play(self) -> int:
        self.played += 1
        return self.get_seed() % self.options

    def get_seed(self) -> int:
        self.seed = (self.seed * (self.played + 1) + self.won + 997) % 9999991
        return self.seed
