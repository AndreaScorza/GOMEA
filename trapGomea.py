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
        temp = []
        for y in range(0, l):
            temp.append(np.random.rand())
        pop.append(temp)
        popByte.append(list(randint(2, size=l)))
    return pop, popByte

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
    if counter >= 9 or fit == (l / k) or allElem(popByte):
        return True
    return False

def generationalPrinting():
    return 0

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
        lT = lt.getLinkageTree(population)
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
        #print(counter, " : ", bestFit)

    return population, popByte, bestFit, counter
    #return population, popByte, bestFit, time.time() - startTime, counter





pop, popByte, bestFit, counter = GOMEA()
print("best fitness : ", bestFit)
for x in popByte:
    print(x)

'''for i in range(0, 4):
    T = time.time()
    pop, popByte, bestFit, counter = GOMEA()
    print(i, ": gen_count : ", counter, " Fitness : ", bestFit, " time : ", round(time.time() - T, 2))

'''