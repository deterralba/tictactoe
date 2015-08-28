from Simulation import InteractionLevel

class Game:
    """"
    Main object, registers the Board and the Players.
    Attributes:
        - boardAR (BoardAndRules)
        - player1 and player2 (Player)
        - lastPlayer and nextPlayer (Player) references to player1 and 2, used for elegance
        - movements (list of Movement) the chronological list of Movement() played
        - states (list of BoardState) the chronological list of BoardStates()
        - turn (int) the present turn of the game, initialised at 0,
            first turn must be 1 (modified in start() )
        - winner (Player or None) defined by board.thereIsAWinner(), stays None is there is none
        - interactionLevel (InteractionLevel) used to define the level of printed outputs

    Methods:
        - start(): starts a game and plays until it is over,
            updates "turn" and checks is the game is over after each movement
    """

    def __init__(self):
        self.boardAR = None
        self.player1 = None
        self.player2 = None
        self.nextPlayer = None
        self.lastPlayer = None
        self.turn = 0
        self.movements = []
        self.states = []
        self.winner = None
        self.interactionLevel = InteractionLevel()

    def start(self):
        # initialisation/reset of the game
        self.player1.order = 1
        self.player2.order = 2
        self.turn = 0
        self.movements = []
        self.states = []
        self.boardAR.reset()

        self.nextPlayer = self.player1
        self.lastPlayer = self.player2

        # loop calling the player as long as their is no winner or the board is not full
        while self.turn < 9 and not self.boardAR.thereIsAWinner():
            self.turn += 1
            self.nextPlayer.play()
            if self.interactionLevel.showEveryMovement:
                print(self.boardAR)
                input("Press Enter")

            # next and last player are switched (via temp_player)
            temp_player = self.nextPlayer
            self.nextPlayer = self.lastPlayer
            self.lastPlayer = temp_player

        # end of the game, we saves the stats of the players
        self.player1.endOfGame()
        self.player2.endOfGame()

        # time to print info if desired by the user (through the interactionLevel object)
        if self.interactionLevel.showFinalBoard:
            print(self.boardAR)
            if self.boardAR.thereIsAWinner():
                print("The winner is player {}!".format(self.winner.order))
            else:
                print("Even")
            print("== Game is over ==")

