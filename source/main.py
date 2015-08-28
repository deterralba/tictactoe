from BoardAndRules import BoardAndRules
from Player import Player
from Game import Game
from Simulation import Simulation
from HumanPlayer import HumanPlayer
from LinePlayer import LinePlayer
from HAL1Player import HAL1Player


testG = Game()
testB = BoardAndRules(testG)
testP1 = Player(testG, testB)
testP2 = Player(testG, testB)
testLP1 = LinePlayer(testG, testB)
testLP2 = LinePlayer(testG, testB)
testHP = HumanPlayer(testG, testB)

testHAL1 = HAL1Player(testG, testB)

testGCfg = Simulation(testG)
testGCfg.interactionLevel.showEveryMovement = False
testGCfg.interactionLevel.showPlayerDebug = False

testGCfg.numberOfGames = 10000

testG.boardAR = testB
testG.player1 = testP1
testG.player2 = testHAL1
# testHAL1.openTraining("trainingHAL1.pickle")

testGCfg.start()
# testHAL1.saveTraining("trainingHAL1.pickle")

print(testG.player1.statistic)
# print(testHAL1.memories.pastGames)
print("len dico", len(testHAL1.memories.pastGames))
print("nbOfIG", testHAL1.nbOfIntelligentGame)

from Tools import Plot
# Plot.plotTotalRatio(testG.player1)
Plot.plotMovingRatio(testG.player1, window=500)
# print(testG.states[0])
# print(testG.states)

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
