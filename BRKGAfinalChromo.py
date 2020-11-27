from numpy.random import seed
from numpy.random import randint
from numpy.random import rand
import numpy as np

# importing the file for the auction input
import inputBids as auction

# Constants
E = 0.4  # is the ratio of elite
R = 0.2  # ratio or random element
P = 0.6 # probability of selecting key from elite for crossover
# 0.7 462 238640
# 0.6 437 238640

values = auction.getAuction('L2-50-100.txt')
goods = values[0]
bidsValue = values[3]
bids = values[4]



# create a double array of [indices, float[0,1] ]
def createKeysForElement(dimension):
    keys = []
    for x in range(0, dimension):
        keys.append([x, float(rand())])
    return keys


# create the population from the random keys of defined size
def createPopulation(size):
    population = []
    for elem in range(0, size):
        population.append(createKeysForElement(len(bids)))
    return population


def decoder(element, discourage):
    element.sort(reverse=True, key=lambda x: x[1])
    markedGoods = np.zeros(goods)
    fitness = 0
    solution = []

    for x in element:
        flag = False
        for y in bids[x[0]]:
            if markedGoods[y] == 1:
                flag = True  # it means it is present
                if discourage:
                    if x[1] > 0.5:
                        x[1] = 1 - x[1]
        if not flag:  # it means it is not present
            for y in bids[x[0]]:
                markedGoods[y] = 1
                fitness += bidsValue[x[0]]
            solution.append(x)

    element.sort(key=lambda x:x[0])

    return element, fitness

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


def generation(population):
    newGeneration = []
    fitnessOfPopulation = []

    '''lista1 = []
    lista2 = []
    for x in population:
        lista1.append(decoder(x, False)[1])'''

    for x in range(0, len(population)):
        fitnessOfPopulation.append(decoder(population[x], True))  # it returns [population, fitness]

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

    return newGeneration, bestFitness


def BRKGAchromo(populationSize):
    population = createPopulation(populationSize)
    bestFitness = 0
    fitNotIncrease = 0
    generationCount = 0


    storedPop = []

    while fitNotIncrease < 100 and generationCount < 100:
        population, fitness = generation(population)

        if bestFitness == 0:
            bestFitness = fitness
            storedPop = population
            print(generationCount, ": ", fitness)
        else:
            if fitness <= bestFitness:
                fitNotIncrease += 1
                print(generationCount, ": ", bestFitness)

            else:
                bestFitness = fitness
                fitNotIncrease = 0
                storedPop = population
                print(generationCount, ": ", bestFitness, " -> ", fitness)

        generationCount += 1

    return bestFitness, storedPop, population



bestFitness, storedPop, lastPopulation = BRKGAchromo(10)
print("best fitness = ", bestFitness)
'''for x in range(0, len(storedPop)):
    a,b = decoder(storedPop[x], False)
    c,d = decoder(lastPopulation[x], False)
    print(b, " --- ", d)'''



