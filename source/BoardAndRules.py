from Game import Game
from BoardState import BoardState

class BoardAndRules:
    """
    Represents the rules of the game,
    saves the present state of the game and checks that the players follow the rules

    Attributes:
        - game (Game) reference to the game
        - boardS (BoardState) representing the present board

    Methods:
        - play(mvt): called by the players, writes "player.order" (1 or 2) on the board
            where the player plays if the place is empty (0)
            Returns True if the movement was legal, else do nothing and returns False
        - extractLines(): returns a list of all the lines that can be completed
        - thereIsAWinner(): returns True if there is a winner and sets game.winner
        - getBoard(): returns a copy of self.boardS, used to store the different state of a game
        - reset(): resets the board for a new game
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

        Also sets movement.turn and registers the movement in the list game.movements
        Registers boardS in game.states

        :param mvt: (Movement) the Movement the player wants to play
        :return: (bool) True if the movement is possible, else False
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
        Extracts the 8 lines than can be completed (3 vertical, 3 horizontal, 2 diagonal: 11-33 and 31-13).

        :return: the list of lines
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
        Sets game.winner if there is one.

        :return: True if there is a winner (ie if 3 dots are aligned), else False
        """
        lines = self.extractLines()
        for line in lines:
            if line[0] != 0 and line[0] == line[1] == line[2]:
                self.game.winner = self.game.lastPlayer
                return True
        return False

    def getBoard(self):
        """
        :return: a copy of the self.board that will not be updated when a new movement is made
        """
        return self.boardS.copy()

    def reset(self):
        """
        Resets the state for a new game
        """
        self.boardS.reset()
