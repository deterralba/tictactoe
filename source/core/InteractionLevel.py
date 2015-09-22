

class InteractionLevel:
    """
    This object is used to store the parameters of the simulation.

    Attributes
    ----------
    showEveryMovement : bool
        Print the state of the game after every movement
    showEveryMovementAndWait : bool
        Print the state of the game after every movement and wait that the user press enter to continue
    showFinalBoard : bool
        Print the final state of the game
    showElapsedTime : bool
        Print the total time that the simulation took
    showPlayerDebug : bool
        Print the debug messages of each player
    """
    def __init__(self):
        self.showEveryMovement = True
        self.showEveryMovementAndWait = False
        self.showFinalBoard = False
        self.showElapsedTime = True
        self.showPlayerDebug = False
