from src.bot import Bot


class TestBot:
    def test_init(self):
        bot = Bot()
        assert isinstance(bot, Bot)

    def test_bot_play(self):
        bot = Bot()
        for _ in range(3):
            assert bot.play() in [0, 1, 2]
        assert bot.played == 3
        assert bot.play() == 2

    def test_get_seed(self):
        bot = Bot()
        assert bot.get_seed() != bot.get_seed()
        assert bot.get_seed() == 1002974
