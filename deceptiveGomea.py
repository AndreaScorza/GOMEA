import numpy as np
import linkageTree as lt
import time
from numpy.random import randint
import random
import orderingProblemValues as order

# global variable
k = 4
l = 32

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


def getFitness(elemByte):
    fitness = 0
    for x in range(0, int(len(elemByte)/k)):
        fitness += order.getValue(elemByte[x:x+k], 'absolute')
    return round(fitness, 2)

def getDonor(population, popByte, x):
    numbers = list(range(0, len(popByte)))
    numbers.remove(x)
    donorIndex = random.choice(numbers)
    return population[donorIndex], popByte[donorIndex]

def checkIfElemInPopulation(elem, pop):
    if pop == []:
        return False
    else:
        for x in range(0, len(pop)):
            if elem == pop[x]:
                print("Element already present in population, discarted!")
                return True
        return False

def greedyRecomb(sol, solByte, donor, donorByte, subset, population):
    #print("Another recombination")
    accepted = 0
    discarted = 0
    for cluster in subset:
        solFit = getFitness(solByte)
        newSol = sol.copy()
        newSolByte = solByte.copy()
        for element in cluster:
            newSol[element] = donor[element]
            newSolByte[element] = donorByte[element]

        newSolFit = getFitness(newSolByte)
        bestFit = solFit

        if newSolFit > solFit:
            accepted += 1
            if not checkIfElemInPopulation(newSol, population):
                sol = newSol
                solByte = newSolByte
                bestFit = newSolFit
        else:
            discarted += 1
    #print("Accepted : ", accepted, " Discarted : ", discarted)
    return sol, solByte, bestFit


# return true if the element of the population are all the same
def allElem(pop):
    for x in range(1, len(pop)):
        if pop[0] != pop[x]:
            return False
    return True

def terminated(counter, fit, popByte):
    if counter >= 30 or fit == l or allElem(popByte):
        return True
    return False

def generationalPrinting():
    return int(0)



def GOMEA():
    #startTime = time.time()
    counter = 0
    population, popByte = createPop(100)
    '''for x in population:
        print(x)'''
    '''for x in popByte:
        print (x)'''
    bestFit = 0
    while not terminated(counter, bestFit, popByte):
        # insert here the ordering of the population
        lT = lt.getLinkageTree(population)
        # translate the linkage tree
        for x in lT:
            print(x)
        print()
        for x in range(0, len(population)):
            for subset in lT[:-1]:  # avoiding the root of the tree
                donor, donorByte = getDonor(population, popByte, x)
                population[x], popByte[x], fit = greedyRecomb(population[x], popByte[x], donor, donorByte, subset, population)
                if bestFit < fit:
                    bestFit = fit
        counter += 1

        #print(counter, " : ", bestFit, " time: ", round(time.time() - startTime, 2))
        print(counter, " : ", bestFit)
        for z in popByte:
            print(z)

    return population, popByte, bestFit, counter
    #return population, popByte, bestFit, time.time() - startTime, counter





pop, popByte, bestFit, counter = GOMEA()
print("best fitness : ", bestFit)


'''for x in popByte:
    print(x)'''

'''for i in range(0, 4):
    T = time.time()
    pop, popByte, bestFit, counter = GOMEA()
    print(i, ": gen_count : ", counter, " Fitness : ", bestFit, " time : ", round(time.time() - T, 2))

'''