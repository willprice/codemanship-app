class Player(object):
    def __init__(self, name):
        self.name = name
        self.games = set()

    def add_games(self, list_of_games):
        self.games = self.games.union(list_of_games)
