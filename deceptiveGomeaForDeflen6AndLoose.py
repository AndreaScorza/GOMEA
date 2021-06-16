import numpy as np
import linkageTree as lt
import time
from numpy.random import randint
import random
import orderingProblemValues as ord

# global variable
k = 4
l = 32
fitnessList = []
#type = 'loose'
#order = 'absolute'
#popSize = 0
# fitEval = [31-1] * 2 * popSize ... for each generation
fitnessEvaluation = 0

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
    return stringToAnalyze#[0]

def getSub(string, type):
    subs = []
    #print(type(string))
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
    global fitnessEvaluation
    fitness = 0
    correctSub = 0
    for x in subs:
        fitness += ord.getValue(x, order)
        if x == [1, 2, 3, 4]:
            correctSub += 1
    fitnessEvaluation += 1
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

def greedyRecomb(sol, solByte, donor, donorByte, subset, population, type, order):
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

        newSolFit, correctSub = getFitness(getSub(orderString(newSol, newSolByte), type), order)
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
    #if counter >= 100 or fit == l or allElem(popByte) or fitnessEvaluation > 2000000: #  or notProgress > 100:
    if fitnessEvaluation > 2000000: #  or notProgress > 100:
        return True
    return False

def GOMEA(popSize, order, type):
    global fitnessEvaluation
    global fitnessList
    fitnessList = []
    startTime = time.time()
    counter = 0
    population, popByte = createPop(popSize)

    bestFit = 0
    notProgress = 0
    listCorrect = []
    tmpList = []
    for x in range(0, len(popByte)):
        a, b = getFitness(getSub(orderString(population[x], popByte[x]), type), order)
        fitnessList.append(a)
        tmpList.append(b)

    print("Initial max value: ", max(fitnessList))
    bestCorrect = max(tmpList)
    fitnessEvaluation = len(population)
    listCorrect.append([counter, fitnessEvaluation, bestCorrect])
    #print()

    while not terminated(counter, bestFit, popByte, notProgress):
        listCorrectTemp = []
        listFit = []
        lastRoundPopulation = population.copy()


        lT = lt.getLinkageTree(population)
        # to create the random linkage tree comment up and uncomment down:
        #a, b = createPop(popSize)
        #lT = lt.getLinkageTree(a)

        #for x in lT[:-1]:
        #    print(x)
        #print()
        for x in range(0, len(population)):
            for subset in lT[:-1]:  # avoiding the root of the tree
                donor, donorByte = getDonor(population, popByte, x)
                population[x], popByte[x], fit, correctSub = greedyRecomb(population[x], popByte[x], donor, donorByte, subset, population, type, order)
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
        #listCorrect.append([counter, bestCorrect])
        listCorrect.append([counter, fitnessEvaluation, bestCorrect])
        #print("counter :" , counter, " bestFit: ", bestFit, " bestCorrect: ", bestCorrect, " time: ", round(time.time() - startTime, 2), " Fit Eval: ", fitnessEvaluation)
        #for z in popByte:
        #    print(z)

        numberOfChange = howManyOfThePopChanged(lastRoundPopulation, population)
        #print("this generation ", numberOfChange," individuals changed")
        if numberOfChange == 0:
            notProgress += 1
        else:
            notProgress = 0
    print(listCorrect)
    #return population, popByte, bestFit, time.time() - startTime, counter, listCorrect
    return listCorrect

##### popsize, type,    order
#GOMEA(10,     'absolute', 'loose')

#pop, popByte, bestFit, time, counter, listCorrect = GOMEA()
'''print()
print("finished")

print("best fitness : ", bestFit, " counter:", counter, "N fit eval: ", fitnessEvaluation)

print(listCorrect)
'''


