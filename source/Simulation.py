import time
from InteractionLevel import InteractionLevel

class Simulation:
    # TODO: add comments here
    def __init__(self, game):
        self.numberOfGames = 1
        self.game = game
        self.exchangePlayers = False
        self.elapsedTime = 0
        self.interactionLevel = InteractionLevel()

    def start(self):
        self.game.interactionLevel = self.interactionLevel
        start_time = time.time()
        for i in range(self.numberOfGames):
            self.game.start()
            if self.exchangePlayers:
                self.game.player1, self.game.player2 = self.game.player2, self.game.player1
        self.elapsedTime = time.time() - start_time
        if self.interactionLevel.showElapsedTime:
            print("Elapsed time: {:.0f}ms".format(1000*self.elapsedTime))

