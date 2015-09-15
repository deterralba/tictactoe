

class Movement:
    """
    Represents a movement played by a player.

    Attributes
    ----------
    place : 2-list of int
        The place [line, column].
    turn : int
        Must be set in board.play().
    player : Player
        The player playing.

    Parameters
    ----------
    player: Player
    place: 2-list of int

    Warning
    -------
    :attr:`self.turn` must be set in :meth:`.BoardAndRules.play`.

    """
    def __init__(self, player, place):
        self.place = place
        self.player = player
        self.turn = 0

    def __str__(self):
        return "Turn {}: movement of player {} is {}".format(self.turn,
                                                             self.player.order,
                                                             self.place)
