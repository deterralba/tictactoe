import time
from InteractionLevel import InteractionLevel

class Simulation:
    def __init__(self, game):
        self.numberOfGames = 1
        self.game = game
        self.elapsedTime = 0
        self.interactionLevel = InteractionLevel()

    def start(self):
        self.game.interactionLevel = self.interactionLevel
        start_time = time.time()
        for i in range(self.numberOfGames):
            self.game.start()
        self.elapsedTime = time.time() - start_time
        if self.interactionLevel.showElapsedTime:
            print("Elapsed time: {:.0f}ms".format(1000*self.elapsedTime))

