from core import *


class Memory:
    def __init__(self):
        self.pastGames = {}

    def addGame(self, game):
        """
        Add a game in the dictionary :attr:`pastGames` :

            - key = hash of the state before the wining movement
            - value = the ``Movement.place`` (couple [x,y]) that linked to the victory

        Parameters
        ----------
        game : Game
            the ended :class:`Game` instance to save

        Warnings
        --------
        Does not check is the result is an even or a victory
        """
        boardSBeforeEnd = game.states[-2]
        winningMovementPlace = game.movements[-1].place
        self.pastGames[boardSBeforeEnd] = winningMovementPlace
