import unittest

from game import Game


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def roll_many(self, pins, times):
        for i in range(times):
            self.game.roll(pins)

    def test_gutter_game(self):
        self.roll_many(pins=0, times=20)

        assert self.game.score == 0

    def test_all_ones(self):
        self.roll_many(pins=1, times=20)

        assert self.game.score == 20

