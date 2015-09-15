

class BoardState:
    """
    Represents the *physical board*.

    Attributes
    ----------
    state: 3-list (line) of 3-list (column)
        The state of the board: initialised with "0": ``[[0, 0, 0], [0, 0, 0], [0, 0, 0]]``
        uses player.order to put "1" or "2" where the players play.


    Parameters
    ----------
    hash: int, optional
        If ``hash`` is in **kwargs, it will be used to fill the board, default is None.

    Examples
    --------
    emptyB = BoardState()
    fullB = BoardState(hash=122121121)


    """

    def __init__(self, hash=None):
        """
        Initialises the board: creates empty state [] and calls :meth:`reset`

        If optimal hash is given, :meth:`unhash` is called
        """
        self.state = []
        self.reset()

        if hash is not None:
            self.unhash(hash)

    def reset(self):
        """ Reset self.state for a new game: to ``[[0, 0, 0], [0, 0, 0], [0, 0, 0]]`` """
        self.state.clear()
        self.state = [[0 for i in range(3)] for j in range(3)]  # generate [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        """
        Return
        ------
        string
            3 lines representing the board (plus one line above and one under)
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
        """
        Return
        ------
        int
            the turn of the board: counts the 0 and deduces the turn ``T = 9 - nb(0)``
        """
        count0 = 0
        for i in range(len(self.state)):
            count0 += self.state[i].count(0)
        return 9 - count0

    def copy(self):
        """
        Return
        ------
        BoardState
            A new identical copy of BoardState (useful for storage)

        """
        copyBS = BoardState()
        copyBS.state = [[self.state[i][j] for j in range(3)] for i in range(3)]
        return copyBS

    def __eq__(self, other):
        """
        Return
        ------
        bool
            True if self.state and other.state are equal
        """
        return self.state == other.state

    def __hash__(self):
        """
        Return
        ------
        int
            An integer created by the concatenation of all the cases

        Examples
        --------
        ``[[0, 1, 2], [3, 4, 5], [6, 7, 8]]`` returns ``12345678``

        Warning
        -------
        First 0 is gone!
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

    def unhash(self, theHash):
        # theHash may be a string or a int, it is converted to string anyway
        theHash = str(theHash)
        # the competed with 0
        theHash = "0"*(9-len(theHash)) + theHash
        # and converted to BoardState()
        self.state = [[int(theHash[3*i + j]) for j in range(3)] for i in range(3)]


if __name__ == '__main__':
    b = BoardState()
    b.state[1][1] = 1

    b_ = BoardState()
    b_.state[1][1] = 1
    print("equality '==' test: True?:",b == b_)

    d = BoardState()
    d.state[0][0]= 1
    d.state[0][1]= 2
    d.state[1][2]= 1

    l = [b, d]
    print("owing test: d in l: True?:", d in l)

    print("hash test: ", d, d.__hash__(), "should be 120001000")

    print("copy() test through hash: should be 120001000:", d.copy().__hash__())

    print("test: instantiated from hash: 12000", BoardState(hash=12000))

