import numpy as np
import linkageTree2 as lt
import time
from numpy.random import randint
import random
import orderingProblemValues as order

# global variable
k = 4
l = 20
fitnessList = []

def createPop(size):
    #pop = []
    popByte = []
    block = [1, 2, 3, 4]
    for x in range(0, size):
        #temp = []
        #for y in range(0, l):
        #    temp.append(np.random.rand())
        #pop.append(temp)
        individual = []
        for x in range(0, int(l / k)):
            individual = individual + random.sample(block, len(block))
        popByte.append(individual)
    return popByte # , pop


def getFitness(elemByte):
    fitness = 0
    correctSub = 0
    for x in range(0, int(len(elemByte)/k)):
        fitness += order.getValue(elemByte[(x*k):(x*k+k)], 'relative')
        if elemByte[(x*k):(x*k+k)] == [1,2,3,4]:
            correctSub += 1
    return round(fitness, 2), correctSub


def getDonor(popByte, x):
    numbers = list(range(0, len(popByte)))
    numbers.remove(x)
    donorIndex = random.choice(numbers)  # excluded the right extremity of the interval
    return popByte[donorIndex]

def checkIfElemInPopulation(elem, pop):
    if pop == []:
        return False
    else:
        for x in range(0, len(pop)):
            if elem == pop[x]:
                #print("Element already present in population, discarted!")
                return True
        return False

def greedyRecomb(solByte, donorByte, subset, popByte):
    #print("Another recombination")
    index = popByte.index(solByte)
    accepted = 0
    discarted = 0
    correctSub = 0
    for cluster in subset:
        solByteFit = fitnessList[index]
        newSolByte = solByte.copy()
        for element in cluster:
            newSolByte[element] = donorByte[element]

        newSolByteFit, correctSub = getFitness(newSolByte)
        bestFit = solByteFit

        if newSolByteFit > solByteFit:
            accepted += 1
            solByte = newSolByte
            bestFit = newSolByteFit
            fitnessList[index] = newSolByteFit
        else:
            discarted += 1
    #print("Accepted : ", accepted, " Discarted : ", discarted)
    return solByte, bestFit, correctSub


#  count how many elements changed from two populations
def howManyOfThePopChanged(pop, newPop):
    number = 0
    for x in range(0, len(pop)):
        if pop[x] != newPop[x]:
            number += 1
    return number

# return true if the element of the population are all the same
def allElem(pop):
    for x in range(1, len(pop)):
        if pop[0] != pop[x]:
            return False
    return True

def terminated(counter, fit, popByte, notProgress):
    if counter >= 100 or fit == l or allElem(popByte): #  or notProgress > 100:
        return True
    return False

def generationalPrinting():
    return int(0)



def GOMEA():
    startTime = time.time()
    counter = 0
    popByte = createPop(2000)

    bestFit = 0
    notProgress = 0
    listCorrect = []
    for x in popByte:
        a, b = getFitness(x)
        fitnessList.append(a)
    print("Initial max value: ", max(fitnessList))
    print()

    while not terminated(counter, bestFit, popByte, notProgress):
        listCorrectTemp = []
        lastRoundPopulation = popByte.copy()

        #lT = lt.getLinkageTree(popByte)

        a = createPop(2500)
        lT = lt.getLinkageTree(a)
        for x in lT[:-1]:
            print(x)
        print()
        for x in range(0, len(popByte)):
            for subset in lT[:-1]:  # avoiding the root of the tree
                donorByte = getDonor(popByte, x)
                popByte[x], fit, correctSub= greedyRecomb(popByte[x], donorByte, subset, popByte)
                listCorrectTemp.append(correctSub)
                if bestFit < fit:
                    bestFit = fit
        listCorrect.append([counter, max(listCorrectTemp)])
        counter += 1

        print(counter, " : ", bestFit, " time: ", round(time.time() - startTime, 2))
        #for z in popByte:
        #    print(z)

        numberOfChange = howManyOfThePopChanged(lastRoundPopulation, popByte)
        print("this generation ", numberOfChange," individuals changed")
        if numberOfChange == 0:
            notProgress += 1
        else:
            notProgress = 0
        print(listCorrect)
    return popByte, bestFit, time.time() - startTime, counter, listCorrect





popByte, bestFit, time, counter, listCorrect = GOMEA()
print("best fitness : ", bestFit, " counter:", counter)

print(listCorrect)
for x in popByte:
    a, b = getFitness(x)
    if a == bestFit:
        print(counter , " ", b , " : ", x)


'''for x in popByte:
    print(getFitness(x), " : ", x)'''




