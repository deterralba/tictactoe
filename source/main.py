"""
This is the entry point of the program, the first module executed.

Here you can parameter all the program, no need to read other source files.

How it works!
=============

There are 6 main steps:

#. importation of the useful packages
#. instantiation if the main objects (Game, BoardAndRules and Simulation)
#. instantiation if the players
#. settings of the simulation parameters (choice of the players, of the numbers of games played etc.)
#. execution of the simulation
#. printing of the results

See the commented source code of to configure the simulation and lunch the program.

"""

if __name__ == '__main__':
    # Importation of the core
    # =======================
    # Fear not ! The package core is conceived to be imported that way
    from core import *
    # This importation occupy the following names:
    # BoardAndRules, BoardState, Game, InteractionLevel, Movement, Player, PlayerStatistic, Simulation

    # Importation of players
    # =======================
    from players.HumanPlayer import HumanPlayer
    from players.LinePlayer import LinePlayer
    from players.HAL1Player import HAL1Player


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
    # testHAL1.openTraining("players/trainingHAL1.pickle")  # to import the trained dictionary


    # Simulation parameters
    # =====================
    testSimu.interactionLevel.showEveryMovement = False
    testSimu.interactionLevel.showEveryMovementAndWait = False
    testSimu.interactionLevel.showPlayerDebug = False
    testSimu.interactionLevel.showFinalBoard = True

    # the number of game to simulate
    testSimu.numberOfGames = 10

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

    # testHAL1.saveTraining("players/trainingHAL1.pickle")  # to save the dictionary


    # shows results
    # =============

    # print on the console the statistic of a player
    print(testG.player1.statistic)

    # shows data of self learning player if it played
    if testHAL1 in (testG.player1, testG.player2):
        print("Size of the memory: {}".format(len(testHAL1.memories.pastGames)))
        print("Number of intelligent games played:", testHAL1.nbOfIntelligentGame)

    # plot the evolution of ratios
    # from misc.Tools import Plot
    # Plot.plotTotalRatio(testG.player1)
    # Plot.plotMovingRatio(testG.player1, window=500)
    #
    # import matplotlib.pyplot as plt
    # plt.plot(testHAL1.evolutionOfMemories)
    # plt.title("Evolution of the size of the IA learned dictionary"
    #           "\nwith the number of games played")
    # plt.show(block=True)

def main():
    """ I'm your link to the main module ! """
    # I do nothing except create a link to the module in the documentation :)
    pass
