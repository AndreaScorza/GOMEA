from numpy.random import seed
from numpy.random import randint
from numpy.random import rand
import numpy as np
import time
import statistics as stat

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

def crossOver(sortedPop):
    offspring = []
    parentAindex = randint(0, len(sortedPop))
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

    '''lista1 = []
    lista2 = []
    for x in population:
        lista1.append(decoder(x, False)[1])'''

    for x in range(0, len(population)):
        fitnessOfPopulation.append(decoder(population[x], True, goods, bids, bidsValue))  # it returns [population, fitness]

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
        offSpring = crossOver(sortedPopulation)
        while offSpring in newGeneration:  # check that the offspring is not in the population already
            offSpring = crossOver(sortedPopulation)
        newGeneration.append(offSpring)

    return newGeneration, bestFitness


def BRKGAchromo(populationSize, problem):

    values = auction.getAuction(problem)
    goods = values[0]
    bidsValue = values[3]
    bids = values[4]

    population = createPopulation(populationSize, bids)
    bestFitness = 0
    fitNotIncrease = 0
    generationCount = 0
    startTime = time.time()
    storedPop = []

    while fitNotIncrease < 200 and generationCount < 5000:
        population, fitness = generation(population, goods, bids, bidsValue)

        if bestFitness == 0:
            bestFitness = fitness
            storedPop = population
            #print(generationCount, ": ", fitness, " time: ", round(time.time()-startTime, 2))
        else:
            if fitness <= bestFitness:
                fitNotIncrease += 1
                #print(generationCount, ": ", bestFitness, " time: ", round(time.time()-startTime, 2))

            else:
                bestFitness = fitness
                fitNotIncrease = 0
                storedPop = population
                #print(generationCount, ": ", bestFitness, " -> ", fitness, " time: ", round(time.time()-startTime, 2))

        generationCount += 1

    return bestFitness, storedPop, population, time.time()-startTime, (generationCount-fitNotIncrease) - 1

def runWithStatistics(popSize, nOfLoops, problem):
    storing = []
    fit = []
    gen = []
    count = 0
    for x in range(0, nOfLoops):
        print("RGKA: ", count)
        count += 1
        bestFitness, storedPop, lastPopulation, totalTime, foundAtGen = BRKGAchromo(popSize, problem)
        storing.append([bestFitness, foundAtGen])
        fit.append(bestFitness)
        gen.append(foundAtGen)

    return fit, gen


#runWithStatistics(50, 500)

#bestFitness, storedPop, lastPopulation, totalTime, foundAtGen = BRKGAchromo(500)
#print("\nBest Fitness ", bestFitness, " Total Time: ", totalTime, " Found at Gen: ", foundAtGen)