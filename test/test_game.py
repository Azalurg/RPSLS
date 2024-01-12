from enum import Enum

from src.game import Game
from src.engines import Engine


class BinaryEnum(Enum):
    ZERO = 0
    ONE = 1


get_engine = lambda: Engine([[0, 1], [1, 0]], BinaryEnum)


class TestGame:
    def test_game_init(self):
        game = Game(get_engine(), 0)
        assert isinstance(game, Game)

    def test_game_end(self):
        game = Game(get_engine(), 0)
        game.wins = 5
        game.looses = 4
        game.draws = 17
        assert game.end() == (5, 4, 17, 26)
