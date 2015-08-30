from Movement import Movement
from Game import Game


class Memory:
    def __init__(self):
        self.pastGames = {}

    def addGame(self, game):
        """
        Add a game in the dictionary self.pastGames :
            key = hash of the state before the wining movement
            value = the Movement.place (couple [x,y]) that linked to the victory

        :param game: the ended Game() instance to save

        Warnings:
            - does not check is the result is an even or a victory
        """
        boardSBeforeEnd = game.states[-2]
        winningMovementPlace = game.movements[-1].place
        self.pastGames[boardSBeforeEnd] = winningMovementPlace
