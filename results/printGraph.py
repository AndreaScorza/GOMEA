import ast
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
from scipy import stats

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
    plt.plot(x1, y1, label = 'LT-GOMEA')
    x2, y2 = getXY(file2)
    plt.plot(x2, y2, label = 'UNIVARIATE-GOMEA')
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
    plt.plot(x1, y1, label = 'LT-GOMEA')
    x2, y2 = getXY(file2)
    x2 = list(range(0, len(y2)))
    plt.plot(x2, y2, label = 'UNIVARIATE-GOMEA')
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
    plt.show()
    #plt.savefig("COMPARISON-NORMAL-UNIVARIATE-Generations.png")


def printDeceptive(problemName, file1, file2, file3, saveName):
    x1, y1 = getXY(file1)
    print(y1[len(y1)-1])
    #x1 = list(range(0, len(y1)))
    plt.plot(x1, y1, label = "GOMEA-100")
    print("primo fatto")
    x2, y2 = getXY(file2)
    #print(y2[len(y2) - 1])
    #x2 = list(range(0, len(y2)))

    #plt.plot(x2, y2, label="GOMEA-500")
    print("secondo fatto")

    x3, y3 = getXY(file3)
    #x3 = list(range(0, len(y3)))
    #plt.plot(x3, y3, label="GOMEA-1000")
    plt.xlabel("Number of generations")
    plt.ylabel("Maximum number of correct subproblems")

    plt.ylim(0, 8.3)
    plt.xlim(0, 2100000)
    #plt.xlim(0, 100)
    plt.title(problemName)
    plt.grid()
    plt.legend()
    plt.show()
    #plt.savefig(saveName)

#printGraph('COMPARISON GOMEA', 'GOMEA/GOMEA-L7.txt', 'GOMEA/GOMEA-L7-256-1000-UNIVARIATE_POP60.txt', ' ')
#printGraphFit4Gen('COMPARISON GOMEA', 'GOMEA/GOMEA-L7.txt', 'GOMEA/GOMEA-L7-256-1000-UNIVARIATE_POP60.txt', ' ')
#printDeceptive('Absolute ordering problem, loose coding', 'DECEPTIVE/absoluteloose500.txt', 'absoluteLoose')
#printDeceptive('Relative ordering problem, deflen6 coding', 'DECEPTIVE/relativeDeflen6500.txt', 'relativeDeflen6')
#printDeceptive('Relative ordering problem, loose coding', 'DECEPTIVE/absoluteLoose500.txt', 'DECEPTIVE/relativeLoose500.txt', 'DECEPTIVE/relativeLoose.txt', 'comparisonDeceptiveGomeaGenerations')
#printGraph('L3-100-300', 'brkga-L3-100-300.txt', 'gomea-L3-100-300.txt')
#printGraphFit4Gen('L3-100-300', 'brkga-L3-100-300.txt', 'gomea-L3-100-300.txt')


#printGraph('L7-256-1000', 'BRKGA/brkga-L7.txt', 'GOMEA/gomea-L7.txt')
#printGraphFit4Gen('COMPARISON GOMEA', 'GOMEA/gomea-L7.txt',  'GOMEA/gomea-L7-256-1000-UNIVARIATE.txt', 'GOMEA/gomea-L7-256-1000-RANDOM-TOTAL.txt')
#printGraph('COMPARISON GOMEA', 'GOMEA/gomea-L7.txt',  'GOMEA/gomea-L7-256-1000-UNIVARIATE.txt','GOMEA/gomea-L7-256-1000-RANDOM-TOTAL.txt')
#printGraphFit4Gen('L3-256-100', 'BRKGA/brkga-L3-100-300.txt', 'GOMEA/gomea-L3-100-300.txt', 'BRKGA/brkga-L3-100-300-pop1000.txt')
#printGraphFit4Gen('L6-100-300', 'BRKGA/brkga-L3-100-300.txt', 'GOMEA/gomea-L3-100-300.txt')

#printGraph('L7-100-300', 'brkga-L7-100-300.txt', 'gomea-L7-100-300.txt')
#printGraphFit4Gen('L7-100-300', 'brkga-L7-100-300.txt', 'gomea-L7-100-300.txt')


# HISTOGRAM
'''
x1 = [0,1,2,3,4]
y1 = [3,2,1,0,4]
plt.bar(x1, y1)#, y1)#, label = 'Trap Function')
plt.xlabel("Number of ones")
plt.ylabel("Fitness")
plt.title("TRAP FUNCTION")
plt.grid()
#plt.legend()
#plt.show()
plt.savefig("TRAP-FUNCTION.png")'''

def performTtest(file1, file2, file3, file4):
    res1 = readTxt(file1)
    res2 = readTxt(file2)
    arr1 = []
    arr2 = []
    if file3 != '':
        print("adding file3 and 4 to the test")
        res3 = readTxt(file3)
        res4 = readTxt(file4)
        for x in res3:
            arr1.append(x[-1][2])
        for y in res4:
            arr2.append(y[-1][2])

    for x in res1:
        arr1.append(x[-1][2])
    for y in res2:
        arr2.append(y[-1][2])
    print(stat.mean(arr1), " ", stat.stdev(arr1))
    print(stat.mean(arr2), " ", stat.stdev(arr2))
    print(stats.ttest_ind(arr1, arr2))



#print(stats.ttest_ind(arr1, arr2))

#performTtest('DECEPTIVE/relativeDeflen6500.txt', 'DECEPTIVE/absoluteloose500.txt', 'DECEPTIVE/relativeloose500.txt', 'DECEPTIVE/absoluteDeflen6500.txt')
#performTtest('DECEPTIVE/relativeDeflen6500.txt', 'DECEPTIVE/relativeloose500.txt', 'DECEPTIVE/absoluteDeflen6500.txt', 'DECEPTIVE/absoluteloose500.txt')
performTtest('GOMEA/GOMEA-L7.txt', 'GOMEA/GOMEA-L7-256-1000-UNIVARIATE_POP60.txt', '', 'DECEPTIVE/absoluteloose500.txt')
#print(readTxt('DECEPTIVE/relativeDeflen6500.txt'))
