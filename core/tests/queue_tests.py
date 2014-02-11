import unittest
from mock import Mock, MagicMock
from ..queue import Queue


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.TicTacToe = "TicTacToe"
        self.Chess     = "Chess"
        self.queue     = Queue()

    def test_a_player_can_be_added(self):
        player = self.create_player()
        self.queue.add_player(player)
        self.assertEqual(1, self.get_length_of_queue())

    def test_two_players_can_be_added_sequentially(self):
        player = self.create_player()
        player_two = self.create_player()
        self.queue.add_player(player)
        self.assertEqual(1, len(self.queue))
        self.queue.add_player(player_two)
        self.assertEqual(2, self.get_length_of_queue())

    def test_the_same_player_cannot_be_added_twice(self):
        player = self.create_player()
        self.queue.add_player(player)
        self.queue.add_player(player)
        self.assertEqual(1, self.get_length_of_queue())

    def test_filter_single_player(self):
        player = self.create_player(games=[self.TicTacToe])
        self.queue.add_player(player)
        self.assertItemsEqual([player], self.queue.filter(self.TicTacToe))

    def test_filter_two_players_by_tic_tac_toe(self):
        player = self.create_player(games=[self.TicTacToe])
        player_without_tic_tac_toe = self.create_player()
        self.queue.add_player(player)
        self.queue.add_player(player_without_tic_tac_toe)
        self.assertItemsEqual([player], self.queue.filter(self.TicTacToe))

    def test_filter_two_player_by_chess(self):
        player = self.create_player(games=[self.Chess])
        player_without_chess = self.create_player(games=[self.TicTacToe])
        self.queue.add_player(player)
        self.queue.add_player(player_without_chess)
        self.assertItemsEqual([player], self.queue.filter(self.Chess))

    def create_player(self, games=[]):
        player = Mock()
        player.games = games
        return player

    def get_length_of_queue(self):
        return len(self.queue)


if __name__ == '__main__':
    unittest.main()
