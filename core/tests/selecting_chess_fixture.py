from waferslim.converters import convert_arg, IterableConverter
from mock import Mock
from core.queue import Queue
from core.player import Player
from mock import Mock


class SelectingChessFixture(object):
    @convert_arg(using=IterableConverter())
    def __init__(self, *player_data):
        self.queue = Queue()

        for player in player_data:
            name  = player[0]
            list_of_games = player[1:]

            player = Player(name)
            player.add_games(list_of_games)
            self.queue.add_player(player)

    def add_player(self, name):
        self.queue.add_player(Player(name))

    def player_chooses_game(self, game):
        self.game = game

    def filtered_players(self):
        filtered_players = self.queue.filter(self.game)
        return [player.name for player in filtered_players]
