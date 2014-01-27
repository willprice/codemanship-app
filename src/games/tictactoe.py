#from waferslim.converters import TableTableConstants
from games.game import Game
from waferslim_hooks.decision_table import DecisionTable

class TicTacToe(Game, DecisionTable):
    def setPlayerOne(self, player):
        pass

    def setPlayerTwo(self, player):
        pass

    def setQueue(self, listOfPlayers):
        pass

    def addPlayers(self):
        return True

    def queue(self):
        return []
