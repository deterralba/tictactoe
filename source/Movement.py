

class Movement:
    """
    Represents a movement played by a player

    - place (list of 2 int) the place [line, column]
    - turn (int) must be set in board.play()
    - player (Player) the player playing

    !! turn must be set !!
    """
    def __init__(self, player, place):
        self.place = place
        self.player = player
        self.turn = 0

    def __str__(self):
        return "Turn {}: movement of player {} is {}".format(self.turn,
                                                             self.player.order,
                                                             self.place)
