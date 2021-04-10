import numpy as np
from numpy.random import randint
import random
import orderingProblemValues as ord

k = 4
l = 32
fitnessList = []

def createPop(size):
    pop = []
    popByte = []
    block = [1, 2, 3, 4]
    for x in range(0, size):
        temp = []
        for y in range(0, l):
            temp.append(np.random.rand())
        pop.append(temp)
        individual = []
        for x in range(0, int(l / k)):
            individual = individual + random.sample(block, len(block))
        popByte.append(individual)
    return pop, popByte

def orderString(elem, elemByte):
    element = elem.copy()
    for x in range(0, len(element)):
        saving = [x, element[x]]
        element[x] = saving
    element.sort(reverse=True, key=lambda x: x[1])
    #print(element)
    #print(elemByte)
    stringToAnalyze = []
    for x in range(0, len(element)):
        stringToAnalyze.append(elemByte[element[x][0]])
    return stringToAnalyze[0]

def getSub(string, type):
    subs = []
    if type == 'deflen6':
        sub1 = [string[0], string[2],string[4], string[6]]
        sub2 = [string[1], string[3], string[5], string[7]]
        sub3 = [string[8], string[10], string[12], string[14]]
        sub4 = [string[9], string[11], string[10], string[15]]
        sub5 = [string[16], string[18], string[20], string[22]]
        sub6 = [string[17], string[19], string[21], string[23]]
        sub7 = [string[24], string[26], string[28], string[30]]
        sub8 = [string[25], string[27], string[29], string[31]]
    if type == 'loose':
        sub1 = [string[0], string[8], string[16], string[24]]
        sub2 = [string[1], string[9], string[17], string[25]]
        sub3 = [string[2], string[10], string[18], string[26]]
        sub4 = [string[3], string[11], string[19], string[27]]
        sub5 = [string[4], string[12], string[20], string[28]]
        sub6 = [string[5], string[13], string[21], string[29]]
        sub7 = [string[6], string[14], string[22], string[30]]
        sub8 = [string[7], string[15], string[23], string[31]]
    subs.append(sub1)
    subs.append(sub2)
    subs.append(sub3)
    subs.append(sub4)
    subs.append(sub5)
    subs.append(sub6)
    subs.append(sub7)
    subs.append(sub8)
    return subs

def getFitness(subs, order):
    fitness = 0
    correctSub = 0
    for x in subs:
        fitness += ord.getValue(x, order)
        if x == [1, 2, 3, 4]:
            correctSub += 1
    print("cc : ", fitness)
    return round(fitness, 2), int(correctSub)



newSol, newSolByte = createPop(1)
type = 'deflen6'
order = 'absolute'

string = orderString(newSol, newSolByte)
subs = getSub(string, type)
newSolFit, correctSub = getFitness(subs, order)


#newSolFit, correctSub = getFitness(getSub(orderString(newSol, newSolByte), type), order)
print(newSolFit, correctSub)
#print(order.get)
print(getFitness(getSub(orderString(newSol, newSolByte), type), order))