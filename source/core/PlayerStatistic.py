

class PlayerStatistic:
    def __init__(self, player):
        self.player = player
        self.numberOfVictories = 0
        self.numberOfEvens = 0
        self.numberOfLosses = 0
        self.numberOfGame = 0
        self.listOfTurns = []
        self.listOfResults = []

    def newResult(self, game):
        self.numberOfGame += 1
        if game.boardAR.thereIsAWinner():
            if game.winner is self.player:
                self.numberOfVictories += 1
                self.listOfResults.append("win")
            else:
                self.numberOfLosses += 1
                self.listOfResults.append("loss")
        else:
            self.numberOfEvens += 1
            self.listOfResults.append("even")
        self.listOfTurns.append(game.turn)

    def __str__(self):
        return "Player {} played {} times:\n\t" \
               "{} victories, {} losses, {} evens".format(self.player.order,
                                                          self.numberOfGame,
                                                          self.numberOfVictories,
                                                          self.numberOfLosses,
                                                          self.numberOfEvens)
