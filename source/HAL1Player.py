from Player import Player
from Memory import Memory
from Movement import Movement


class HAL1Player(Player):
    """
    Subclass of Player, first try of learning player
    """
    def __init__(self, game, board):
        super().__init__(game, board)
        self.memories = Memory()
        self.saveGame = True
        self.nbOfIntelligentGame = 0

    def play(self):
        """ Play a first random movement and then tries to play intelligently """
        if self.game.turn <= 2:
            self.randomPlay()
            if self.game.interactionLevel.showPlayerDebug:
                print("HAL1: beginning random")

        elif self.game.boardAR.boardS in self.memories.pastGames:
            place = self.memories.pastGames[self.game.boardAR.boardS]
            mvt = Movement(self, place)
            self.boardAR.play(mvt)

            if self.game.interactionLevel.showPlayerDebug:
                print("HAL1: intelligent !")

            self.nbOfIntelligentGame += 1
            self.saveGame = False
        else:
            if self.game.interactionLevel.showPlayerDebug:
                print("HAL1: not the beginning but random !")
            self.randomPlay()

    def endOfGame(self):
        if self.game.interactionLevel.showPlayerDebug:
            print("HAL1: EOG, saveGame:", self.saveGame)
        if self.saveGame and self.game.winner is not None:
            self.memories.addGame(self.game)
        # if not self.saveGame:
        #     print("If not saveGame", self.game.winner is self)
        self.saveGame = True

    def openTraining(self, trainingFileName):
        import pickle
        with open(trainingFileName, 'rb') as f:
            self.memories.pastGames = pickle.load(f)

    def saveTraining(self, trainingFileName):
        import pickle
        with open('trainingHAL1.pickle', 'wb') as f:
            pickle.dump(self.memories.pastGames, f, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    print([[] for i in range(10)])