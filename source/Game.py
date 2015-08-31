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
        - movements (list of Movement) the list of all the Movements made
        - states (list of BoardStates) the list of the different BoardState of the game
        - winner (Player or None) defined by board.thereIsAWinner(), stays None is there is none
        - interactionLevel (InteractionLevel) used to define the level of printed outputs

    Methods:
        - start(): starts a game and plays until it is over,
            updates "turn" and checks is the game is over after each movement
        - reset(): reset the game (turn, movements, sates, winner, next and last player

    Warnings:
        - movements and states must be updated by boardAR.play()
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
        """
        Plays a game until it is over, i.e. there is a winner or the game is even

        How it is working:
        ------------------
        As long as the game is not over (ie self.turn < 9 and thereIsAWinner == False) there is a loop where
            - turn is incremented,
            - nextPlayer.play() is called and then next and last player are inverted,
            - if wanted, the board is printed.
        When it is over, endOfGame() of player1 and 2 is called - if wanted, the result is printed.
        """
        # prepares all the instances (board etc) for a new game
        self.reset()

        self.nextPlayer = self.player1
        self.lastPlayer = self.player2

        # loop calling the player as long as their is no winner or the board is not full
        while self.turn < 9 and not self.boardAR.thereIsAWinner():
            self.turn += 1
            self.nextPlayer.play()
            if self.interactionLevel.showEveryMovement or self.interactionLevel.showEveryMovementAndWait:
                print(self.boardAR)
                if self.interactionLevel.showEveryMovementAndWait:
                    input("Press Enter")

            # next and last player are switched (via temp_player)
            self.nextPlayer, self.lastPlayer = self.lastPlayer, self.nextPlayer

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

    def reset(self):
        """ Reset the game for a new game """
        self.player1.order = 1
        self.player2.order = 2
        self.turn = 0
        self.movements = []
        self.states = []
        self.boardAR.reset()



