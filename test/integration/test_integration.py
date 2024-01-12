from main import main_loop
from src.game import Game
from src.engines import AdvanceEngine, SimpleEngine


def catch_message(msg) -> bool:
    return msg == "Too many input attempts"


class TestIntegration:
    def test_main(self, monkeypatch):
        inputs = iter(["1", "2", "n"])
        monkeypatch.setattr("builtins.input", lambda msg: next(inputs))
        result = main_loop()
        assert result == 0

    def test_game_advance_1000(self, monkeypatch):
        game = Game(AdvanceEngine())
        monkeypatch.setattr("builtins.input", lambda msg: 1)
        for _ in range(1000):
            game.play()
        assert game.end()[3] == 1000

    def test_game_simple_1000(self, monkeypatch):
        game = Game(SimpleEngine())
        monkeypatch.setattr("builtins.input", lambda msg: 1)
        for _ in range(1000):
            game.play()
        assert game.end()[3] == 1000

    def test_wrong_input(self, monkeypatch):
        inputs = iter(["a", "1", "5", "a", "2", "n"])
        outputs = []

        monkeypatch.setattr("builtins.input", lambda msg: next(inputs))
        monkeypatch.setattr("builtins.print", lambda msg, **kwargs: outputs.append(msg))

        result = main_loop()
        assert result == 0
        assert "Wrong input !!! Expected '1', '2', or '0'" in outputs
        assert "Chosen option not in range" in outputs
        assert "Wrong input" in outputs
