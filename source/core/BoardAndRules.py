from .BoardState import BoardState


class BoardAndRules:
    """
    Represents the rules of the game,
    saves the present state of the game and checks that the players follow the rules.

    Attributes
    ----------
    game : Game
        A reference to the game.
    boardS : BoardState
        Represents the present physical board.
    """

    def __init__(self, game):
        self.game = game
        self.boardS = BoardState()

    def __str__(self):
        representation = "== Tic TaC Toe ==\n" \
                         "Present turn: {}\n".format(self.game.turn)
        return representation + str(self.boardS)

    def play(self, mvt):
        """
        Verifies that the movement of the player follows the rules and writes it on the board.

        Also sets :attr:`.Movement.turn` and registers the movement in the list :attr:`.Game.movements`
        Registers boardS in :attr:`.Game.states`

        Parameters
        ----------
        mvt : Movement
            The Movement the player wants to play

        Returns
        -------
        bool
            True if the movement is possible, else False

        """
        # if the place is empty (occupy by 0), the order of the payer is written in it
        if self.boardS.state[mvt.place[0]][mvt.place[1]] == 0:
            self.boardS.state[mvt.place[0]][mvt.place[1]] = mvt.player.order
            mvt.turn = self.game.turn
            self.game.movements.append(mvt)
            self.game.states.append(self.getBoard())
            return True
        else:
            return False

    def extractLines(self):
        """
        Extracts the 8 lines than can be completed:

        - 3 vertical: left -> right,
        - 3 horizontal: up -> down,
        - 2 diagonal: 11->33 & 31->13.

        Returns
        -------
        list of list
            The list of lines
        """
        board = self.boardS.state
        lines = []

        for i in range(3):
            line_i = board[i]
            lines.append(line_i)

        for i in range(3):
            column_i = [board[j][i] for j in range(3)]
            lines.append(column_i)

        diagonal_1 = [board[i][i] for i in range(3)]
        diagonal_2 = [board[2 - i][i] for i in range(3)]
        lines.append(diagonal_1)
        lines.append(diagonal_2)

        return lines

    def thereIsAWinner(self):
        """
        Sets :attr:`.Game.winner` if there is one.

        Returns
        -------
        bool
            True if there is a winner (ie if 3 dots are aligned), else False
        """
        lines = self.extractLines()
        for line in lines:
            if line[0] != 0 and line[0] == line[1] == line[2]:
                self.game.winner = self.game.lastPlayer
                return True
        return False

    def getBoard(self):
        """
        Returns
        -------
        BoardState
            a copy of the self.board that will not be updated when a new movement is made
        """
        return self.boardS.copy()

    def reset(self):
        """
        Resets the state for a new game
        """
        self.boardS.reset()
