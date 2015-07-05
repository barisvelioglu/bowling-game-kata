class Game(object):
    def __init__(self):
        super(Game, self).__init__()
        self._score = 0
        self._rolls = [0 for i in range(21)]
        self._current_roll = 0

    def roll(self, pins):
        self._rolls[self._current_roll] = pins
        self._current_roll += 1
        self._score += pins

    @property
    def score(self):
        return self._score
