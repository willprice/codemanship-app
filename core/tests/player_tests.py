import unittest
from mock import Mock

from core.player import Player


class PlayerTests(unittest.TestCase):
    def setUp(self):
        self.TicTacToe = "TicTacToe"
        self.Chess     = "Chess"
        self.player = Player("John")

    def test_player_knows_what_games_have_been_added(self):
        self.player.add_games([self.TicTacToe])
        self.assertItemsEqual([self.TicTacToe], self.player.games)

    def test_when_a_game_is_added_others_arent_overwritten(self):
        self.player.add_games([self.TicTacToe])
        self.player.add_games([self.Chess])
        self.assertItemsEqual([self.TicTacToe, self.Chess], self.player.games)

    def test_cannot_add_duplicate_games(self):
        self.player.add_games([self.TicTacToe])
        self.player.add_games([self.TicTacToe])
        self.assertSetEqual(set([self.TicTacToe]), self.player.games)

if __name__ == '__main__':
    unittest.main()
