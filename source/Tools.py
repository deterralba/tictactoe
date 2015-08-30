import math
from Player import Player

#TODO: add comments !
class Analyze:
    @staticmethod
    def createTotalRatios(resultsList):
        length = len(resultsList)
        winRatioList = []
        lossRatioList = []
        evenRatioList = []
        for i in range(length):
            # used to cut the list
            temp_length = i+1
            # print(temp_length, resultsList[:temp_length])
            winRatioList.append(resultsList[:temp_length].count("win")/(temp_length))
            lossRatioList.append(resultsList[:temp_length].count("loss")/(temp_length))
            evenRatioList.append(resultsList[:temp_length].count("even")/(temp_length))
        return [winRatioList, lossRatioList, evenRatioList]

    @staticmethod
    def createMovingRatios(resultsList, window):

        temp_list = resultsList.copy()
        temp_list = Analyze.replaceInList(temp_list, "win", 1)
        temp_list = Analyze.replaceInList(temp_list, "even", 0)
        temp_list = Analyze.replaceInList(temp_list, "loss", 0)
        winRatioList = Analyze.extractMovingAverage(temp_list, window)

        temp_list = resultsList.copy()
        temp_list = Analyze.replaceInList(temp_list, "win", 0)
        temp_list = Analyze.replaceInList(temp_list, "even", 0)
        temp_list = Analyze.replaceInList(temp_list, "loss", 1)
        lossRatioList = Analyze.extractMovingAverage(temp_list, window)

        temp_list = resultsList.copy()
        temp_list = Analyze.replaceInList(temp_list, "win", 0)
        temp_list = Analyze.replaceInList(temp_list, "even", 1)
        temp_list = Analyze.replaceInList(temp_list, "loss", 0)
        evenRatioList = Analyze.extractMovingAverage(temp_list, window)

        return [winRatioList, lossRatioList, evenRatioList]

    @staticmethod
    def replaceInList(l, sample, newSample):
        while l.count(sample) > 0:
            l[l.index(sample)] = newSample
        return l

    @staticmethod
    def extractMovingAverage(list, window):
        length = len(list)
        averageList = []
        for i in range(length//window):
            # used to cut the list
            start = i*window
            stop = (i+1)*window
            averageList.append(sum(list[start:stop])/window)
        return averageList


class Plot:
    @staticmethod
    def writeResultsInConsole(resultsList, precision=10):
        length = len(resultsList)
        winRatio = ""
        lossRatio = ""
        evenRatio = ""
        for i in range(precision):
            # used to cut the list
            temp_length = math.floor((length-1)/precision*(i+1)) + 1
            # print(temp_length, resultsList[:temp_length])
            nbWin = resultsList[:temp_length].count("win")/(temp_length)
            nbLoss = resultsList[:temp_length].count("loss")/(temp_length)
            nbEven = resultsList[:temp_length].count("even")/(temp_length)
            winRatio += "{:.2f} |".format(nbWin)
            lossRatio += "{:.2f} |".format(nbLoss)
            evenRatio += "{:.2f} |".format(nbEven)
        print("W:", winRatio)
        print("L:", lossRatio)
        print("E:", evenRatio)

    @staticmethod
    def plotTotalRatio(player):
        import matplotlib.pyplot as plt
        resultsList = player.statistic.listOfResults
        ratioList = Analyze().createTotalRatios(resultsList)
        winList = ratioList[0]
        lossList = ratioList[1]
        evenList = ratioList[2]
        plt.plot(winList, label="Win")
        plt.plot(lossList, label="Loss")
        plt.plot(evenList, label="Even")
        plt.legend()
        plt.show(block=True)

    @staticmethod
    def plotMovingRatio(player, window=20):
        import matplotlib.pyplot as plt
        resultsList = player.statistic.listOfResults
        ratioList = Analyze().createMovingRatios(resultsList, window)
        winList = ratioList[0]
        lossList = ratioList[1]
        evenList = ratioList[2]
        plt.plot(winList, label="Win")
        plt.plot(lossList, label="Loss")
        plt.plot(evenList, label="Even")
        plt.legend()
        plt.show(block=True)



if __name__ == '__main__':
    print(Analyze.extractMovingAverage([1, 2, 3, 4], 3))
    l = ["win", "win", "loss", "even"]
    t = l.copy()
    t[1] = "loss"
    print(t.index("win"))
    while t.count("win") > 0:
        t[t.index("win")] = 1
    print(l, t)
    print(Analyze.replaceInList(t, "even", "lol"))
    print(Analyze.createMovingRatios(["win", "loss", "loss", "win", "loss", "loss", "even", "loss"], 4))
    pl = Player(None, None)
    pl.statistic.listOfResults = l
    Plot.plotMovingRatio(pl, window=2)

