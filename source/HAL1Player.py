from core import *
from Memory import Memory

class HAL1Player(Player):
    """
    Subclass of Player, first try of learning player
    """
    def __init__(self, game, board):
        super().__init__(game, board)
        self.memories = Memory()
        self.saveGame = True
        self.nbOfIntelligentGame = 0  # used for statistics purposes
        self.evolutionOfMemories = []  # used to record the evolution of the length of the memories' dict

    def play(self):
        """
        Play a first random movement and then tries to play intelligently

        Intelligently means it recognises learned the boardStates that leads to direct victory (in one movement)
        and plays the winning movement --- not so intelligent but self learning !
        """
        # random movement for the first turn
        if self.game.turn <= 2:
            self.randomPlay()
            if self.game.interactionLevel.showPlayerDebug:
                print("HAL1: beginning random")

        # if the boardState is known, the wining movement is played
        elif self.game.boardAR.boardS in self.memories.pastGames:
            place = self.memories.pastGames[self.game.boardAR.boardS]
            mvt = Movement(self, place)
            self.boardAR.play(mvt)

            if self.game.interactionLevel.showPlayerDebug:
                print("HAL1: intelligent !")

            self.nbOfIntelligentGame += 1
            self.saveGame = False
        # else a random movement is played
        else:
            if self.game.interactionLevel.showPlayerDebug:
                print("HAL1: not the beginning but random !")
            self.randomPlay()

    def endOfGame(self):
        """
        Record the game if it is not an already know game

        This function is called when a game is over, it relies on self.saveGame to know if the game must be learn
        or not. If it is the case, memories.addGame(game) is called.
        Reset self.saveGame to True at the end.
        Manages self.evolutionOfMemories
        """
        # calls the parent's method (that registers the statistics)
        super(HAL1Player, self).endOfGame()

        # print info if wanted
        if self.game.interactionLevel.showPlayerDebug:
            print("HAL1: EOG, saveGame:", self.saveGame)

        # if the game is not knows (saveGame == True) and is not even (winner != None)
        # the game is learnt
        if self.saveGame and self.game.winner is not None:
            self.memories.addGame(self.game)

        # reset of self.saveGame (must not be forgotten !)
        self.saveGame = True

        # Add the length of the memory
        self.evolutionOfMemories.append(len(self.memories.pastGames))

    def openTraining(self, trainingFileName):
        """ Imports a trained memories dictionary """
        import pickle
        with open(trainingFileName, 'rb') as f:
            self.memories.pastGames = pickle.load(f)

    def saveTraining(self, trainingFileName):
        """ Saves a trained memories dictionary """
        import pickle
        with open('trainingHAL1.pickle', 'wb') as f:
            pickle.dump(self.memories.pastGames, f, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    print([[] for i in range(10)])
