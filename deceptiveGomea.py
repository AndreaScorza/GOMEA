import numpy as np
import linkageTree as lt
import time
from numpy.random import randint
import random
import orderingProblemValues as order

# global variable
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

# if flag = true it will return the maximum number of correct subproblems
def getFitness(elem, elemByte):
    element = elem.copy()
    for x in range(0, len(element)):
        saving = [x, element[x]]
        element[x] = saving
    element.sort(reverse=True, key=lambda x: x[1])
    fitness = 0
    correctSub = 0
    for x in range(0, int(len(elemByte)/k)):
        stringToAnalyze = []
        for y in range(0, 4):
            stringToAnalyze.append(elemByte[element[x*k+y][0]])
        # fitness += order.getValue(elemByte[(x*k):(x*k+k)], 'absolute')
        fitness += order.getValue(stringToAnalyze, 'relative')
        if stringToAnalyze == [1,2,3,4]:
            correctSub += 1
    return round(fitness, 2), int(correctSub)


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
                #print("Element already present in population, discarted!")
                return True
        return False

def greedyRecomb(sol, solByte, donor, donorByte, subset, population):
    #print("Another recombination")
    index = population.index(sol)
    accepted = 0
    discarted = 0
    bestCorrectSub = 0
    for cluster in subset:
        solFit = fitnessList[index]
        newSol = sol.copy()
        newSolByte = solByte.copy()
        for element in cluster:
            newSol[element] = donor[element]
            newSolByte[element] = donorByte[element]

        newSolFit, correctSub = getFitness(newSol, newSolByte)
        bestFit = solFit

        if newSolFit > solFit:
            accepted += 1
            if not checkIfElemInPopulation(newSol, population):
                sol = newSol
                solByte = newSolByte
                bestFit = newSolFit
                fitnessList[index] = newSolFit
                bestCorrectSub = correctSub
        else:
            discarted += 1
            bestCorrectSub = solFit // k
    #print("Accepted : ", accepted, " Discarted : ", discarted)
    return sol, solByte, bestFit, bestCorrectSub


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

def GOMEA():
    startTime = time.time()
    counter = 0
    population, popByte = createPop(2500)

    bestFit = 0
    notProgress = 0
    listCorrect = []
    tmpList = []
    for x in range(0, len(popByte)):
        a, b = getFitness(population[x], popByte[x])
        fitnessList.append(a)
        tmpList.append(b)

    print("Initial max value: ", max(fitnessList))
    bestCorrect = max(tmpList)
    listCorrect.append([0, bestCorrect])
    print()

    while not terminated(counter, bestFit, popByte, notProgress):
        listCorrectTemp = []
        listFit = []
        lastRoundPopulation = population.copy()


        #lT = lt.getLinkageTree(population)
        # to create the random linkage tree comment up and uncomment down:
        a, b = createPop(2500)
        lT = lt.getLinkageTree(a)

        for x in lT[:-1]:
            print(x)
        print()
        for x in range(0, len(population)):
            for subset in lT[:-1]:  # avoiding the root of the tree
                donor, donorByte = getDonor(population, popByte, x)
                population[x], popByte[x], fit, correctSub = greedyRecomb(population[x], popByte[x], donor, donorByte, subset, population)
                #listCorrectTemp.append(correctSub)
                #listFit.append(fit)
                if bestCorrect < correctSub:
                    bestCorrect = correctSub
                if bestFit < fit:
                    bestFit = fit
        counter += 1
        #print(sorted(listCorrectTemp, reverse=True))
        #print(sorted(listFit, reverse=True))
        #print(sorted(fitnessList, reverse=True))

        #listCorrect.append([counter, max(listCorrectTemp)])
        listCorrect.append([counter, bestCorrect])
        print("counter :" , counter, " bestFit: ", bestFit, " bestCorrect: ", bestCorrect, " time: ", round(time.time() - startTime, 2))
        #for z in popByte:
        #    print(z)

        numberOfChange = howManyOfThePopChanged(lastRoundPopulation, population)
        print("this generation ", numberOfChange," individuals changed")
        if numberOfChange == 0:
            notProgress += 1
        else:
            notProgress = 0
        print(listCorrect)
    return population, popByte, bestFit, time.time() - startTime, counter, listCorrect





pop, popByte, bestFit, time, counter, listCorrect = GOMEA()
print()
print("finished")

print("best fitness : ", bestFit, " counter:", counter)

import progressBar as pb

for x in range(0, len(popByte)):
    a, b, c = pb.getFitness(pop[x], popByte[x])
    if a == bestFit:
        print(a, " ", b, " : ", popByte[x], " ", c)
print()
print(listCorrect)



