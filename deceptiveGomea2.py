import numpy as np
import linkageTree as lt
from time import time
from numpy.random import randint
import random
import orderingProblemValues as order
# global variable
k = 4
l = 32

# without biased random key

def createPop(size):
    popByte = []
    block = [1, 2, 3, 4]
    for x in range(0, size):
        individual = []
        for x in range(0, int(l / k)):
            #tail = random.sample(block, len(block))
            #individual = np.concatenate((individual, tail))
            individual = individual + random.sample(block, len(block))
        popByte.append(individual)
    return popByte

def getFitness(elemByte):
    fitness = 0
    for x in range(0, int(len(elemByte)/k)):
        fitness += order.getValue(elemByte[x:x+k], 'absolute')
    return round(fitness, 2)

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

def greedyRecomb(solByte, donorByte, subset):
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
    # print("Accepted : ", accepted, " Discarted : ", discarted)
    return solByte, bestFit

# return true if the element of the population are all the same
def allElem(pop):
    for x in range(1, len(pop)):
        if pop[0] != pop[x]:
            return False
    return True

def terminated(counter, fit, pop):
    if counter >= 30 or fit == l or allElem(pop):
        return True
    return False

def generationalPrinting():
    return int(0)

def GOMEA():

    counter = 0
    popByte = createPop(100)
    for x in popByte:
        print(x)

    bestFit = 0
    while not terminated(counter, bestFit, popByte):
        lT = lt.getLinkageTree(popByte)
        for x in lT:
            print(x)
        print()
        for x in range(0, len(popByte)):
            for subset in lT[:-1]:  # avoiding the root of the tree
                donorByte = getDonor(popByte, x)
                popByte[x], fit = greedyRecomb(popByte[x], donorByte, subset)
                if bestFit < fit:
                    bestFit = fit
        counter += 1
        #print(counter, " : ", bestFit, " time: ", round(time.time() - startTime, 2))
    #return popByte, bestFit, time() - start_t, counter
    print(counter, " : ", bestFit)
    for z in popByte:
        print(z)
    return popByte, bestFit, counter



popByte, bestFit, counter = GOMEA()
print("best fitness : ", bestFit)
'''for x in popByte:
    print(x)'''

'''for i in range(0, 4):
    popByte, bestFit, counter = GOMEA()
    print(i, ": gen_count : ", counter, " Fitness : ", bestFit)'''

'''for i in range(0, 4):
    popByte, bestFit, time, counter = GOMEA()
    print(counter, " : ", bestFit, " time: ", time)'''



