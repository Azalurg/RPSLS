from src.engines import *


class TestEngines:
    def test_simple_engine_init(self):
        simple_engine = SimpleEngine()
        assert isinstance(simple_engine, SimpleEngine)
        assert isinstance(simple_engine, Engine)

    def test_simple_engine_get_results(self):
        simple_engine = SimpleEngine()
        assert simple_engine.get_result(2, 0) == -1
        assert simple_engine.get_result(2, 1) == 1
        assert simple_engine.get_result(1, 1) == 0

    def test_simple_engine_get_string(self):
        simple_engine = SimpleEngine()
        assert simple_engine.get_string(0) == "Rock"
        assert simple_engine.get_string(1) == "Paper"
        assert simple_engine.get_string(2) == "Scissors"

    def test_advance_engine_init(self):
        advance_engine = AdvanceEngine()
        assert isinstance(advance_engine, AdvanceEngine)
        assert isinstance(advance_engine, Engine)

    def test_advance_engine_get_results(self):
        advance_engine = AdvanceEngine()
        assert advance_engine.get_result(3, 0) == -1
        assert advance_engine.get_result(2, 1) == 1
        assert advance_engine.get_result(4, 4) == 0

    def test_advance_engine_get_string(self):
        advance_engine = AdvanceEngine()
        assert advance_engine.get_string(0) == "Rock"
        assert advance_engine.get_string(2) == "Scissors"
        assert advance_engine.get_string(4) == "Spock"