import unittest
from mock import Mock
from core.queue import Queue
from core.player import Player

# Run with mocks? Uncomment this line
#Player = Mock

class QueueTests(unittest.TestCase):
    def setUp(self):
        self.TicTacToe = "TicTacToe"
        self.Chess     = "Chess"
        self.queue     = Queue()

    def test_a_player_can_be_added(self):
        player = self.create_player()
        self.add_player_to_queue(player)
        self.assertEqual(1, self.get_length_of_queue())

    def test_two_players_can_be_added_sequentially(self):
        players = self.create_players(2)
        self.add_player_to_queue(players[0])
        self.assertEqual(1, self.get_length_of_queue())
        self.add_player_to_queue(players[1])
        self.assertEqual(2, self.get_length_of_queue())

    def test_the_same_player_cannot_be_added_twice(self):
        player = self.create_player()
        self.add_player_to_queue(player)
        self.add_player_to_queue(player)
        self.assertEqual(1, self.get_length_of_queue())

    def test_filter_single_player(self):
        player = self.create_player(games=[self.TicTacToe])
        self.add_player_to_queue(player)
        self.assertItemsEqual([player], self.queue.filter(self.TicTacToe))

    def test_filter_two_players_by_tic_tac_toe(self):
        player = self.create_player(games=[self.TicTacToe])
        player_without_tic_tac_toe = self.create_player()
        self.add_player_to_queue(player)
        self.add_player_to_queue(player_without_tic_tac_toe)
        self.assertItemsEqual([player], self.queue.filter(self.TicTacToe))

    def test_filter_two_player_by_chess(self):
        player = self.create_player(games=[self.Chess])
        player_without_chess = self.create_player(games=[self.TicTacToe])
        self.add_player_to_queue(player)
        self.add_player_to_queue(player_without_chess)
        self.assertItemsEqual([player], self.queue.filter(self.Chess))

    def test_add_players_to_queue(self):
        number_of_players = 2
        players = self.create_players(number_of_players)
        self.add_players_to_queue(players)
        self.assertEqual(number_of_players, self.get_length_of_queue())

    def create_player(self, games=[], name="John"):
        player = Player(name)
        player.games = games
        return player

    def create_players(self, number_of_players, games=[]):
        players = []
        for _ in range(number_of_players):
            player = self.create_player(games=games)
            players.append(player)
        return players

    def get_length_of_queue(self):
        return len(self.queue)

    def add_players_to_queue(self, players):
        self.queue.add_players(players)

    def add_player_to_queue(self, player):
        self.queue.add_player(player)

if __name__ == '__main__':
    unittest.main()
