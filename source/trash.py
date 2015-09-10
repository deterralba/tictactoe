"""
This is a test file used as a Python interpreter.. Chunks of more or less useful pices of code!
"""

if __name__ == '__main__':

    t = [[1, 2, 3, 4], [10, 20, 30]]
    print([t[i] for i in range(len(t))])


    state = []
    for i in range(3):
        state.append([0, 0, 0])
    state[0][1] = 2
    print(state)
    for i in range(3):
        print([state[j][i] for j in range(3)])

    line = [0, 0, 10]
    if line[0] == line[1] == line[2]:
        print("over !")

    import time
    print(time.time())

    class TestC:
        def __init__(self, name):
            self.name = name

    t1 = TestC("A")
    t2 = TestC("A")

    if t1==t2: print("==")
    else: print("not ==")
    if t1 is t1: print("is")
    else: print("not is")
    if t1 is TestC: print("is Class")
    else: print("not is Class")

    print([1, 2, 3, 4][:3])

    l = [[1, 2], [3, 2], [2, 2], [1, 4]]
    if [1, 4] in l:
        print("L in 4")
    print(len([[2,1], [2,1], [2,1], 1]))

    print("//", 16//4)

    print(3 in [[3], 4])

    def testFun():
        return bool([True for i in range(3) if i==7])

    print(testFun())
    print([[1, 2, 2], [1, 3]] == [[1, 2, 2], [1, 2]])

    l = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    print([i for subi in l for i in subi])