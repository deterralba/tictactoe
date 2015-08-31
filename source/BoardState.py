

class BoardState:
    """
    Represents the "physical board"

    Attributes:
    - state (list of list) 3-list (line) of 3-list (column),
        initialised with "0",
        uses player.order to put "1" or "2" where the players play.

    Methods:
        - reset() empty to board
        - len() return the turn
        - __eq__() compare two boardState
    """

    def __init__(self):
        """ Initialises the board: creates empty state [] and calls self.reset() """
        self.state = []
        self.reset()

    def reset(self):
        """ Reset self.state for a new game: to [[0, 0, 0], [0, 0, 0], [0, 0, 0]] """
        self.state.clear()
        self.state = [[0 for i in range(3)] for j in range(3)]  # generate [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        """
        Returns a string of 3 lines (plus one above and one under) representing the board,
        with X and O instead of 1 and 2
        """
        grid = ""
        for i in range(3):
            grid += "\n\t {} | {} | {} ".format(self.state[i][0],
                                                self.state[i][1],
                                                self.state[i][2])
        grid = grid.replace(" 0 ", "   ")
        grid = grid.replace(" 1 ", " X ")
        grid = grid.replace(" 2 ", " O ")
        grid += "\n"
        return grid

    def __len__(self):
        """ Returns the turn of the board (counts the 0 and deduces the turn T = 9 - nb(0) )"""
        count0 = 0
        for i in range(len(self.state)):
            count0 += self.state[i].count(0)
        return 9 - count0

    def copy(self):
        """ Creates a new object BoardState identical and returns it (used for storage) """
        copyBS = BoardState()
        copyBS.state = [[self.state[i][j] for j in range(3)] for i in range(3)]
        return copyBS

    def __eq__(self, other):
        """ Tests the equality of self.state and other.state """
        return self.state == other.state

    def __hash__(self):
        """
        Returns a integer created by the concatenation of all the cases
        Ex: [[0, 1, 2], [3, 4, 5], [6, 7, 8]] returns 12345678 (NB: first 0 is gone !)
        """
        # flatten the list and convert item to string, ex: [[0,1,2], [3,4,5]] -> ['0','1','2','3','4','5']
        flat_list = [str(i) for sublist in self.state for i in sublist]
        strResult = "".join(flat_list)  # concatenate the list into a string, ex: [1, 2, 3, 4] -> "1234"

        # --- old equivalent code ---
        # strResult = ""
        # for i in range(3):
        #     for j in range(3):
        #         strResult += "{}".format(self.state[i][j])
        return int(strResult)



if __name__ == '__main__':
    b = BoardState()
    c = BoardState()
    d = BoardState()
    b.state[1][1]= 1
    c.state[1][1]= 1

    d.state[0][0]= 1
    d.state[0][1]= 2
    d.state[1][2]= 1
    # print(len(b))
    # print([b, b])
    print(b == c, b != c)
    l = [b, c]
    print(c in l)
    dd = {}
    dd[2] = "lol2"
    dd["k"] = "lolk"
    print(d.__hash__())
    # dd[b] = "BS B"
    print(d.copy().__hash__())

