from BoardAndRules import BoardAndRules
from Player import Player
from Game import Game
from Simulation import Simulation
from HumanPlayer import HumanPlayer
from LinePlayer import LinePlayer
from HAL1Player import HAL1Player

if __name__ == '__main__':

    # principal objects are instantiated
    # ==================================
    testG = Game()
    testB = BoardAndRules(testG)
    testSimu = Simulation(testG)


    # the different players are instantiated
    # ======================================

    # NB an instance of a player cannot play directly against itself because of the attribute self.order
    # random players
    testP1 = Player(testG, testB)
    testP2 = Player(testG, testB)
    # linear player (tries to complete lines)
    testLP1 = LinePlayer(testG, testB)
    # human player
    testHP = HumanPlayer(testG, testB)
    # first self-leaning player
    testHAL1 = HAL1Player(testG, testB)
    # testHAL1.openTraining("trainingHAL1.pickle")  # to import the trained dictionary

    # Simulation parameters
    # =====================
    testSimu.interactionLevel.showEveryMovement = False
    testSimu.interactionLevel.showEveryMovementAndWait = False
    testSimu.interactionLevel.showPlayerDebug = False
    testSimu.interactionLevel.showFinalBoard = True

    # the number of game to simulate
    testSimu.numberOfGames = 10000

    # exchange the two players at the end of each game, makes an even series of game fair
    testSimu.exchangePlayers = False

    testG.boardAR = testB  # the game needs to have a reference to the board
    # defines the players of the simulation
    testG.player1 = testP1
    testG.player2 = testHAL1

    # shows the board if there is a human player
    if testHP in (testG.player1, testG.player2):
        testSimu.interactionLevel.showEveryMovement = True


    # starts the simulation
    # =====================
    testSimu.start()

    # testHAL1.saveTraining("trainingHAL1.pickle")  # to save the dictionary


    # shows results
    # =============

    # print on the console the statistic of a player
    print(testG.player1.statistic)

    # shows data of self learning player if it played
    if testHAL1 in (testG.player1, testG.player2):
        print("Size of the memory: {}".format(len(testHAL1.memories.pastGames)))
        print("Number of intelligent games played:", testHAL1.nbOfIntelligentGame)

    # plot the evolution of ratios
    # from Tools import Plot
    # Plot.plotTotalRatio(testG.player1)
    # Plot.plotMovingRatio(testG.player1, window=500)
    #
    # import matplotlib.pyplot as plt
    # plt.plot(testHAL1.evolutionOfMemories)
    # plt.title("Evolution of the size of the IA learned dictionary"
    #           "\nwith the number of games played")
    # plt.show(block=True)





    # --- old debugging ---
    # while True:
    # testG.start()
    # place = [1, 2]
    # testB.play(testP1, place)
    # testB.play(testP2, [1, 1])
    # print(testB)
    # k = 0
    # for i in range(3):
    #     for j in range(3):
    #         k += 1
    #         testB.state[i][j] = k
    # print(testB.state)
