import random
from .PlayerStatistic import PlayerStatistic
from .Movement import Movement


class Player:
    """"
    Represents a random player, is subclassed to create human and intelligent players

    Attributes
    ----------
    boardAR : BoardAndRules
        A reference to the board (and rules)
    game : Game
        A reference to the game
    order : int
        Tells if the player is the first to play or the second,
        is used to select the type of mark used on the board
        !! initialised with -1, must be set !!
    statistic : PlayerStatistic
        Saves the stats of the player

    Warnings
    --------
    player.order must be set by the game
    """

    def __init__(self, game, boardAR):
        self.game = game
        self.boardAR = boardAR
        self.order = -1
        self.statistic = PlayerStatistic(self)

    def play(self):
        """ Calls randomPlay() """
        self.randomPlay()

    def randomPlay(self):
        """ Play a random movement (stupid: tries until a movement is not refused) """
        movement = Movement(self, [random.randint(0, 2), random.randint(0, 2)])
        movementIsAccepted = self.boardAR.play(movement)
        if not movementIsAccepted:
            self.randomPlay()

    def endOfGame(self):
        self.statistic.newResult(self.game)
