import unittest

from game import Game


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_gutter_game(self):
        times = 20
        pins = 0
        self.roll_many(pins, times)

        assert self.game.score == 0

    def roll_many(self, pins, times):
        for i in range(times):
            self.game.roll(pins)

    def test_all_ones(self):

        for i in range(20):
            self.game.roll(1)

        assert self.game.score == 20

