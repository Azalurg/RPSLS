class Engine:
    def __init__(self, conditions):
        self.conditions = conditions

    def get_result(self, player: int, bot: int) -> int:
        return self.conditions[player][bot]


class SimpleEngine(Engine):
    def __init__(self):
        conditions = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
        super().__init__(conditions)


class AdvanceEngine(Engine):
    def __init__(self):
        conditions = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0],
        ]
        super().__init__(conditions)
