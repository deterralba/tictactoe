from Player import Player
from Movement import Movement

class HumanPlayer(Player):
    """ Subclass of Player, asks via the command prompt where to play (line and column, between 1 and 3) """
    def __init__(self, game, boardAR):
        super().__init__(game, boardAR)

    def play(self):
        raw_line = input("Line? (1, 2, 3)")
        raw_column = input("Column? (1, 2, 3)")
        # the input must be strings 1, 2 or 3, else the function is called again
        if raw_column in ["1", "2", "3"] and raw_line in ["1", "2", "3"]:
            # when shift from 123 (human) to 012 (python)
            line = int(raw_line) - 1
            column = int(raw_column) - 1
            # the movement is created and tried, if impossible (case occupied), the function is called again
            movement = Movement(self, [line, column])
            movementIsAccepted = self.boardAR.play(movement)
            if not movementIsAccepted:
                print("Wrong input ! Try again")
                self.play()
        else:
            print("Wrong input ! Try again")
            self.play()
