class Queue(object):
    def __init__(self):
        self.players = set()

    def __len__(self):
        return len(self.players)

    def __iter__(self):
        return iter(self.players)

    def add_player(self, player):
        self.players.add(player)

    def filter(self, game):
        filtered_queue = Queue()
        for player in self.players:
            if game in player.games:
                filtered_queue.add_player(player)
        return filtered_queue
