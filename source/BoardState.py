

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
        self.state = []
        for i in range(3):
            self.state.append([0, 0, 0])

    def reset(self):
        self.state = []
        for i in range(3):
            self.state.append([0, 0, 0])

    def __repr__(self):
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
        count0 = 0
        for i in range(len(self.state)):
            count0 += self.state[i].count(0)
        return 9 - count0

    def copy(self):
        copyBS = BoardState()
        for i in range(3):
            for j in range(3):
                copyBS.state[i][j] = self.state[i][j]
        return copyBS

    def __eq__(self, other):
        for i in range(3):
            if self.state[i] != other.state[i]:
                return False
        return True

    def __hash__(self):
        strResult = ""
        for i in range(3):
            for j in range(3):
                strResult += "{}".format(self.state[i][j])
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
    print(len(b))
    print([b, b])
    print(b == c, b != c)
    l = [b, c]
    print(c in l)
    dd = {}
    dd[2] = "lol2"
    dd["k"] = "lolk"
    print(d.__hash__())
    # dd[b] = "BS B"
    print(d)

