from numpy.random import seed
from numpy.random import randint
from numpy.random import rand
import numpy as np
import time


# importing the file for the auction input
import inputBids as auction

# Constants
E = 0.4  # is the ratio of elite
R = 0.2  # ratio or random element
P = 0.6 # probability of selecting key from elite for crossover
# 0.7 462 238640
# 0.6 437 238640




# create a double array of [indices, float[0,1] ]
def createKeysForElement(dimension):
    keys = []
    for x in range(0, dimension):
        keys.append([x, float(rand())])
    return keys


# create the population from the random keys of defined size
def createPopulation(size, bids):
    population = []
    for elem in range(0, size):
        population.append(createKeysForElement(len(bids)))
    #print(population[0])
    return population


def decoder(element, discourage, goods, bids, bidsValue):

    element.sort(reverse=True, key=lambda x: x[1])

    markedGoods = np.zeros(goods)
    fitness = 0
    for x in element:
        flag = False
        for y in bids[x[0]]:
            if markedGoods[y] == 1:
                flag = True
                if discourage:
                    if x[1] > 0.5:
                        x[1] = 1 - x[1]
        if not flag:
            fitness += bidsValue[x[0]]
            for y in bids[x[0]]:
                markedGoods[y] = 1
    element.sort(key=lambda x: x[0])
    return element, round(fitness, 5)

def crossOver(sortedPop, nOfElite):
    offspring = []
    parentAindex = randint(0, nOfElite)
    parentBindex = randint(0, len(sortedPop))
    while parentAindex == parentBindex:
        parentBindex = randint(0, len(sortedPop))

    parentA = sortedPop[parentAindex]
    parentB = sortedPop[parentBindex]

    for x in range(0, len(parentA)):
        if len(parentA) != len(parentB):
            print(("different lenghts of parents !!! parentA: ", len(parentA), " parentB: ", len(parentB)))
        else:
            if rand() <= P:
                offspring.append(parentA[x])
            else:
                offspring.append(parentB[x])

    return offspring


def generation(population, goods, bids, bidsValue):
    newGeneration = []
    fitnessOfPopulation = []
    nFitEval = 0

    '''lista1 = []
    lista2 = []
    for x in population:
        lista1.append(decoder(x, False)[1])'''

    for x in range(0, len(population)):
        fitnessOfPopulation.append(decoder(population[x], True, goods, bids, bidsValue))  # it returns [population, fitness]
        nFitEval += 1

    # here we order the list of [element, fitness] by its fitness
    fitnessOfPopulation.sort(reverse=True, key=lambda x:x[1])
    sortedPopulation = []
    bestFitness = fitnessOfPopulation[0][1]


    for x in fitnessOfPopulation:
        sortedPopulation.append(x[0])  # now we have the population sorted

    '''for x in sortedPopulation:
        lista2.append(decoder(x, False)[1])
    for x in range(0, len(lista1)):
        print(lista1[x], " --- ", lista2[x])'''

    nOfElite = int(len(population) * E)
    nOfRandom = int(len(population) * R)
    nOfCrossOver = len(population) - (nOfElite + nOfRandom)

    for x in range(0, nOfElite):
        newGeneration.append(sortedPopulation[x])
    for x in range(0, nOfRandom):
        newGeneration.append(createKeysForElement(len(bids)))

    for x in range(0, nOfCrossOver):
        offSpring = crossOver(sortedPopulation, nOfElite)
        while offSpring in newGeneration:  # check that the offspring is not in the population already
            offSpring = crossOver(sortedPopulation, nOfElite)
        newGeneration.append(offSpring)

    return newGeneration, bestFitness, nFitEval


def BRKGAchromo(populationSize, problem):
    values = auction.getAuction(problem)
    goods = values[0]
    bidsValue = values[3]
    bids = values[4]

    # -----
    storingList = []
    population = createPopulation(populationSize, bids)
    # i am creating a copy of the population just to be sure to not mess with the original population
    popCopy = population.copy()
    fitlist = []
    for x in popCopy:
        a, b = decoder(x, False, goods, bids, bidsValue)
        fitlist.append(b)
    storingList.append([0, len(popCopy), max(fitlist)])
    # -----

    bestFitness = 0
    fitNotIncrease = 0
    generationCount = 0
    startTime = time.time()
    storedPop = []
    totFitEval = 0

    while fitNotIncrease < 200 and generationCount < 10000:
    #while (generationCount * len(population)) < 12200:
        population, fitness, nFitEval = generation(population, goods, bids, bidsValue)
        totFitEval += nFitEval

        if bestFitness == 0:
            bestFitness = fitness
            storedPop = population
            print(generationCount, ": ", fitness, " time: ", round(time.time()-startTime, 2))
            print("Number of fitness evaluation for this generation: ", nFitEval)
        else:
            if fitness <= bestFitness:
                fitNotIncrease += 1
                print(generationCount, ": ", bestFitness, " time: ", round(time.time()-startTime, 2))
                print("Number of fitness evaluation for this generation: ", nFitEval)


            else:
                bestFitness = fitness
                fitNotIncrease = 0
                storedPop = population
                print(generationCount, ": ", bestFitness, " -> ", fitness, " time: ", round(time.time()-startTime, 2))
                print("Number of fitness evaluation for this generation: ", nFitEval)

        generationCount += 1
        storingList.append([generationCount, len(population) * (generationCount + 1), bestFitness])

    #return bestFitness, storedPop, population, time.time()-startTime, (generationCount-fitNotIncrease) - 1, totFitEval, values, storingList
    return storingList

#print(BRKGAchromo(5, "L4-5-5.txt"))
'''
def runWithStatistics(popSize, nOfLoops, problem):
    storing = []
    fit = []
    gen = []
    count = 0
    for x in range(0, nOfLoops):
        print("BRGKA: ", count)
        count += 1
        bestFitness, storedPop, lastPopulation, totalTime, foundAtGen, totFitEval, values = BRKGAchromo(popSize, problem)
        storing.append([bestFitness, foundAtGen])
        fit.append(bestFitness)
        gen.append(foundAtGen)

    #for x in range(0, len(storing)):
    #    print(x, " ", storing[x])

    return fit, gen


bestFitness, storedPop, lastPopulation, totalTime, foundAtGen, totFitEval, values, storingList = BRKGAchromo(5, "L4-5-5.txt")
print("finished ", storingList)
goods = values[0]
bidsValue = values[3]
bids = values[4]

#runWithStatistics(50, 500)

print(goods)
print(bidsValue)
print(bids)
for x in storedPop:
    print(decoder(x, False, goods, bids, bidsValue))

#bestFitness, storedPop, lastPopulation, totalTime, foundAtGen, totFitEval = BRKGAchromo(300, "L1-250-1000.txt")
print("\nBest Fitness ", bestFitness, " Total Time: ", totalTime, " Found at Gen: ", foundAtGen)
#print("Total number of fitness evaluations: ", totFitEval)'''




