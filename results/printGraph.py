import ast
import matplotlib.pyplot as plt
import statistics as stat

def readTxt(name):
    arr = []
    lines = filter(None, (line.rstrip() for line in open(name)))
    for line in lines:
        arr.append(ast.literal_eval(line))
    return arr

def makeSameLength(name):
    arr = readTxt(name)

    for x in arr:
        print(max(x))

    listLen = []
    for x in arr:
        listLen.append(max(x)[0])
    maxLen = max(listLen)
    for x in arr:
        while len(x) <= maxLen:
            x.append([len(x), x[0][1] + (len(x) * x[0][1]), x[len(x)-1][2]])
    return arr

# x stands for fitness evaluation, y stands for fitness
def getXY(name):
    arr = makeSameLength(name)
    x = []
    y = []
    for i in range(0, len(arr[0])):  # da 0 a 4
        tmp = []
        for j in range(0, len(arr)):  # da 0 a 3
            tmp.append(arr[j][i][2])
        x.append(arr[0][i][1])
        y.append(stat.mean(tmp))

    return x, y


def printGraph(problemName, file1, file2):
    x1, y1 = getXY(file1)
    plt.plot(x1, y1, label = 'BRKGA')
    x2, y2 = getXY(file2)
    plt.plot(x2, y2, label = 'GOMEA')
    plt.xlabel("Fitness Evaluations")
    plt.ylabel("Fitness")
    plt.title(problemName)
    plt.legend()
    plt.show()

def printGraphFit4Gen(problemName, file1, file2):
    x1, y1 = getXY(file1)
    plt.plot(x1, y1, label = 'BRKGA')
    x2, y2 = getXY(file2)
    plt.plot(x2, y2, label = 'GOMEA')
    plt.xlabel("Fitness Evaluations")
    plt.ylabel("Fitness")
    plt.title(problemName)
    plt.legend()
    plt.show()

printGraph('L3-100-300', 'brkga-L3-100-300.txt', 'gomea-L3-100-300.txt')








