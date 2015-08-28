from Movement import Movement
from Game import Game


class Memory:
    def __init__(self):
        self.pastGames = {}

    def addGame(self, game):
        boardSBeforeEnd = game.states[-2]
        winningMovementPlace = game.movements[-1].place
        self.pastGames[boardSBeforeEnd] = winningMovementPlace
