import unittest

from game import Game


class TestBowlingGame(unittest.TestCase):
    def test_gutter_game(self):
        game = Game()

        for i in range(20):
            game.roll(0)

        assert game.score == 0

    def test_all_ones(self):
        game = Game()

        for i in range(20):
            game.roll(1)

        assert game.score == 20

