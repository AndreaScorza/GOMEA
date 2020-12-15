import numpy as np
import linkageTree as lt
import time
from numpy.random import randint
import random

# global variable
k = 5
l = 20
#byteArray = np.random.randint(2, size=l)
def createPop(size):
    pop = []
    popByte = []
    for x in range(0, size):
        popByte.append(list(randint(2, size=l)))
    return popByte

def switch(i):
    switcher = {
        0: 0.8,
        1: 0.6,
        2: 0.4,
        3: 0.2,
        4: 0,
        5: 1
    }
    return switcher.get(i,"Invalid")

def getFitness(elemByte):
    #print(elemByte)
    fitness = 0
    for x in range(0, int(len(elemByte)/5)):
        sumU = 0 # count how many 1 in the substring
        for y in range(0, 5):
            sumU += elemByte[x*k+y]
        #print(sumU)
        #print(switch(sumU))
        fitness += switch(sumU)

    return round(fitness, 2) # 2 decimal point for safety

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
                print("Element already present in population, discarted!")
                return True
        return False

def greedyRecomb(solByte, donorByte, subset, population):
    #print("Another recombination")
    accepted = 0
    discarted = 0
    for cluster in subset:
        solByteFit = getFitness(solByte)
        newSolByte = solByte.copy()
        for element in cluster:
            newSolByte[element] = donorByte[element]

        newSolByteFit = getFitness(newSolByte)
        bestFit = solByteFit

        if newSolByteFit > solByteFit:
            accepted += 1
            solByte = newSolByte
            bestFit = newSolByteFit
        else:
            discarted += 1
    #print("Accepted : ", accepted, " Discarted : ", discarted)
    return solByte, bestFit

def terminated(counter):
    if counter > 10:
        return True
    return False

def generationalPrinting():
    return 0

def GOMEA():
    startTime = time.time()
    counter = 0
    popByte = createPop(10)
    for x in popByte:
        print (x)
    bestFit = 0
    while not terminated(counter):
        lT = lt.getLinkageTree(popByte)
        for x in range(0, len(popByte)):
            for subset in lT[:-1]:  # avoiding the root of the tree
                donorByte = getDonor(popByte, x)
                popByte[x], fit = greedyRecomb(popByte[x], donorByte, subset, popByte)
                if bestFit < fit:
                    bestFit = fit
        counter += 1
        print(counter, " : ", bestFit, " time: ", round(time.time() - startTime, 2))
    return popByte, bestFit, time.time() - startTime




#popByte, bestFit, time = GOMEA()

'''for x in popByte:
    print (x)
'''
popByte = createPop(100)
for x in range(0, len(popByte)):
    donorByte = getDonor(popByte, x)
    #print(popByte.index(donorByte), " e ", x)
    while popByte.index(donorByte) == x:
        print("dentro ", popByte.index(donorByte), " e ", x)
        donorByte = getDonor(popByte)
    #print("final ", popByte.index(donorByte), " e ", x)

randint(0, len(popByte))