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


def printGraph(problemName, file1, file2, file3):
    x1, y1 = getXY(file1)
    plt.plot(x1, y1, label = 'GOMEA')
    x2, y2 = getXY(file2)
    plt.plot(x2, y2, label = 'GOMEA UNIVARIATE')
    '''x3, y3 = getXY(file3)
    plt.plot(x3, y3, label='pop 1000')'''
    plt.xlabel("Fitness Evaluations")
    plt.ylabel("Fitness")
    plt.title(problemName)
    plt.grid()
    plt.legend()
    #plt.show()
    plt.savefig("COMPARISON-NORMAL-UNIVARIATE.png")

def printGraphFit4Gen(problemName, file1, file2, file3):
    x1, y1 = getXY(file1)
    x1 = list(range(0, len(y1)))
    plt.plot(x1, y1, label = 'GOMEA')
    x2, y2 = getXY(file2)
    x2 = list(range(0, len(y2)))
    plt.plot(x2, y2, label = 'GOMEA UNIVARIATE')
    '''x3, y3 = getXY(file3)
    for x in range(0, len(x3)):
        x3[x] /= 1000
    print(type(x3[0]))
    print(x3)
    plt.plot(x3, y3, label='pop 1000')'''
    plt.xlabel("Number of Generations")
    plt.ylabel("Fitness")
    plt.title(problemName)
    plt.grid()
    plt.legend()
    #plt.show()
    plt.savefig("COMPARISON-NORMAL-UNIVARIATE-Generations.png")

#printGraph('L3-100-300', 'brkga-L3-100-300.txt', 'gomea-L3-100-300.txt')
#printGraphFit4Gen('L3-100-300', 'brkga-L3-100-300.txt', 'gomea-L3-100-300.txt')


#printGraph('L7-256-1000', 'BRKGA/brkga-L7.txt', 'GOMEA/gomea-L7.txt')
#printGraphFit4Gen('COMPARISON GOMEA', 'GOMEA/gomea-L7.txt',  'GOMEA/gomea-L7-256-1000-UNIVARIATE.txt', 'GOMEA/gomea-L7-256-1000-RANDOM-TOTAL.txt')
printGraph('COMPARISON GOMEA', 'GOMEA/gomea-L7.txt',  'GOMEA/gomea-L7-256-1000-UNIVARIATE.txt','GOMEA/gomea-L7-256-1000-RANDOM-TOTAL.txt')
#printGraphFit4Gen('L3-256-100', 'BRKGA/brkga-L3-100-300.txt', 'GOMEA/gomea-L3-100-300.txt', 'BRKGA/brkga-L3-100-300-pop1000.txt')
#printGraphFit4Gen('L6-100-300', 'BRKGA/brkga-L3-100-300.txt', 'GOMEA/gomea-L3-100-300.txt')

#printGraph('L7-100-300', 'brkga-L7-100-300.txt', 'gomea-L7-100-300.txt')
#printGraphFit4Gen('L7-100-300', 'brkga-L7-100-300.txt', 'gomea-L7-100-300.txt')





