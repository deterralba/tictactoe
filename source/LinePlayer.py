from Player import Player
from Movement import Movement
import random

class LinePlayer(Player):
    """
    Subclass of Player, first move is random, then check if there is an unoccupied line with 2
    cases already checked by itself and check the last case, (if there is none do the same
    with a free line where there is already one case checked)
    """
    def __init__(self, game, boardAR):
        super().__init__(game, boardAR)

    def play(self):
        """ Play a first random movement and then tries to complete lines """
        if self.game.turn <= 2:
            if self.game.interactionLevel.showPlayerDebug:
                print("LP: Random")
            self.randomPlay()
        else:
            lines = self.boardAR.extractLines()
            casesForLine = [[[0, 0], [0, 1], [0, 2]],  # line 1
                            [[1, 0], [1, 1], [1, 2]],
                            [[2, 0], [2, 1], [2, 2]],
                            [[0, 0], [1, 0], [2, 0]],  # column 1
                            [[0, 1], [1, 1], [2, 1]],
                            [[0, 2], [1, 2], [2, 2]],
                            [[0, 0], [1, 1], [2, 2]],  # diagonal up left - down rigth
                            [[2, 0], [1, 1], [0, 2]]]
            for i in range(8):
                countSelf = lines[i].count(self.order)
                countFree = lines[i].count(0)
                if countSelf == 2 and countFree == 1:
                    freeCaseIndex = lines[i].index(0)
                    mvt = Movement(self, casesForLine[i][freeCaseIndex])
                    self.boardAR.play(mvt)
                    if self.game.interactionLevel.showPlayerDebug:
                        print("LP: 2 occupied / 1 free", freeCaseIndex, casesForLine[i][freeCaseIndex])
                    return
            for i in range(8):
                countSelf = lines[i].count(self.order)
                countFree = lines[i].count(0)
                if countSelf == 1 and countFree == 2:
                    freeCaseIndex = lines[i].index(0)
                    mvt = Movement(self, casesForLine[i][freeCaseIndex])
                    self.boardAR.play(mvt)
                    if self.game.interactionLevel.showPlayerDebug:
                        print("LP: 1 occupied / 2 free", freeCaseIndex, casesForLine[i][freeCaseIndex])
                    return
            if self.game.interactionLevel.showPlayerDebug:
                print("LP: random > 1")
            movement = Movement(self, [random.randint(0, 2), random.randint(0, 2)])
            movementIsAccepted = self.boardAR.play(movement)
            if not movementIsAccepted:
                self.play()