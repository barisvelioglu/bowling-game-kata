class Game(object):
    def __init__(self):
        super(Game, self).__init__()
        self._score = 0

    def roll(self, pins):
        self._score += pins

    @property
    def score(self):
        return self._score
