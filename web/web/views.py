from django.db import models
from django.shortcuts import render
from core.player import Player
from core.queue import Queue

def index(request):
    will = Player("Will")
    will.add_games(["TicTacToe"])
    jason = Player("Jason")
    jason.add_games(["TicTacToe", "Poker"])
    queue = Queue()
    queue.add_players([will, jason])
    games = ["TicTacToe", "Chess", "Poker"]
    context = {'queue': queue, 'games': games}
    return render(request, 'web/index.html', context)
