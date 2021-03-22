from numpy.random import seed
from numpy.random import randint
from numpy.random import rand
import numpy as np


import inputBids as auction
# Constants
E = 0.4  # is the ratio of elite
R = 0.2  # ratio or random element
P = 0.6  # probability of selecting key from elite for crossover
T = 0.5  # threshold

#seed(1)
# randint(1, 100, 50)
# rand(5)

# goods = randint(1, 100, 20)  # 20 goods
'''goods = 20
bids = [[1, 2], [1, 4], [3, 5, 9], [7, 13, 18], [20, 15, 4], [5, 6, 7, 8], [9, 3, 19], [17, 18, 19, 4, 2], [13],
        [14, 7, 6], [12, 11], [10, 9, 5], [17, 1, 20], [19], [16, 13, 12], [14, 15], [1, 17, 9], [4, 5, 8], [1, 9],
        [14]]  # 20 bids
bidsValue = randint(1, 1000, len(bids))  # tha values of every bid (correspond to the index)

'''
values = auction.getAuction('L1-250-1000.txt')
goods = values[0]
bidsValue = values[3]
bids = values[4]
# create a double array of [indices, float[0,1] ]
def createKeysForElement(dimension):
    keys = []
    for x in range(0, dimension):
        keys.append([x, float(rand(1))])
    return keys


# to sort the keys in non increasing order

def nonIncreasingOrder(elem, numberOfElement):
    elem.sort(reverse=True, key=lambda x: x[numberOfElement])  # sorted in non increaing order
    return elem


# create the population from the random keys of defined size
def createPopulation(size):
    population = []
    for elem in range(0, size):
        # population.append(random.sample(keyList, len(keyList)))
        population.append(createKeysForElement(len(bids)))
    return population


# return just the keys, from the keys and indices array
def returnListOfKeys(keys):
    return np.hsplit(np.array(keys), 2)[1]


def checkIfBidAvailable(markedGoods, index):
    for z in bids[index]:
        if markedGoods[z - 1] == 1:
            return False
    return True


def markTheGoods(markedGoods, index):
    for x in bids[index]:
        if markedGoods[x - 1] == 1:
            return ("Trying to mark an already marked good")
        else:
            markedGoods[x - 1] = 1
    return markedGoods


# return the solution and fitness for one element
def DecodereChromosomalApproach(element):
    markedGoods = np.zeros(goods)
    solution = []
    fitness = 0
    element = nonIncreasingOrder(element, 1)

    for x in element:
        if checkIfBidAvailable(markedGoods, x[0]):
            solution.append(x)
            markedGoods = markTheGoods(markedGoods, x[0])
            fitness += bidsValue[x[0]]
    return [solution, fitness]  # we're storing also the solution, but it's probably not important


def costBenefitCalc(elem):
    b = bidsValue[elem[0]]
    B = len(bids[0])
    return b / B


def decoderGreedyApproach(element2):
    element = []
    for x in element2:
        element.append(x)
    markedGoods = np.zeros(goods)
    solution = []
    fitness = 0

    # removing under threshold T and adding cost benefit
    listRemainingBids = []
    for x in (element):
        if x[1] < T:
            listRemainingBids.append(x)
        else:
            costBenefit = costBenefitCalc(x)
            x.append(costBenefit)
    for x in listRemainingBids:
        element.remove(x)

    # ordering by cost benefit
    element = nonIncreasingOrder(element, 2)  # two is the index of the third element

    for x in element:
        if checkIfBidAvailable(markedGoods, x[0]):
            solution.append(x)
            markedGoods = markTheGoods(markedGoods, x[0])
            fitness += bidsValue[x[0]]
        else:
            if x[1] > 0.5:
                x[1] = 1 - x[1]  # discourage the bid for future generations

    # now processing the remaining bids
    for x in (listRemainingBids):
        costBenefit = costBenefitCalc(x)
        x.append(costBenefit)

    listRemainingBids = nonIncreasingOrder(listRemainingBids, 2)
    for x in listRemainingBids:
        if checkIfBidAvailable(markedGoods, x[0]):
            solution.append(x)
            markedGoods = markTheGoods(markedGoods, x[0])
            fitness += bidsValue[x[0]]
        else:
            if x[1] < 0.5:
                x[1] = 1 - x[1]  # encourage the bid for future generations

    finalElement = []  # we return this element with encouraged and discouraged bids
    for x in element:
        x.remove(x[2])
        finalElement.append(x)
    for x in listRemainingBids:
        x.remove(x[2])
        finalElement.append(x)

    # we return the element with the updated keys
    # il fitness qua è un elemento, invece dovrebbe essere una lista
    finalElement.sort(key=lambda x: x[0])

    return [solution, fitness, finalElement]


def decoderForSolution(element2):
    element = []
    for x in element2:
        element.append(x)
    markedGoods = np.zeros(goods)
    fitness = 0

    # removing under threshold T and adding cost benefit
    listRemainingBids = []
    for x in (element):
        if x[1] < T:
            listRemainingBids.append(x)
        else:
            costBenefit = costBenefitCalc(x)
            x.append(costBenefit)
    for x in listRemainingBids:
        element.remove(x)

    # ordering by cost benefit
    element = nonIncreasingOrder(element, 2)  # two is the index of the third element

    for x in element:
        if checkIfBidAvailable(markedGoods, x[0]):
            markedGoods = markTheGoods(markedGoods, x[0])
            fitness += bidsValue[x[0]]

    # now processing the remaining bids
    for x in (listRemainingBids):
        costBenefit = costBenefitCalc(x)
        x.append(costBenefit)

    listRemainingBids = nonIncreasingOrder(listRemainingBids, 2)
    for x in listRemainingBids:
        if checkIfBidAvailable(markedGoods, x[0]):
            markedGoods = markTheGoods(markedGoods, x[0])
            fitness += bidsValue[x[0]]

    finalElement = []  # we return this element with encouraged and discouraged bids
    for x in element:
        x.remove(x[2])
        finalElement.append(x)
    for x in listRemainingBids:
        x.remove(x[2])
        finalElement.append(x)

    # we return the element with the updated keys
    # il fitness qua è un elemento, invece dovrebbe essere una lista

    finalElement.sort(key=lambda x: x[0])

    return [fitness, finalElement]



# just to visualize the population
def printPopulation(population):

    fitnessArray = []
    for x in range(0, len(population)):
        print(population[x])
        a, population[x] = decoderForSolution(population[x])
        fitnessArray.append(a)
    return fitnessArray

# print the indices of the bids of the population, divided by element of the population
def printIndicesOfBidOfPopulation(population, fitnessArray):
    a = 0
    for x in population:
        array = []
        for y in x:
            array.append(y[0])

        print(array, sum(array), " fitness: ", fitnessArray[a])
        a += 1


def sortPopulationByFitness(population):
    sortedPopulation = []
    for x in range(0, len(population)):
        sortedPopulation.append(
            [x, DecodereChromosomalApproach(population[x])[1]])  # [1] so it's the fitness and not the solution
    return (nonIncreasingOrder(sortedPopulation, 1))


def sortPopulationByFitnessGreedy(population):
    listPosssibleBestSolution = []
    sortedPopulation = []
    populationWithAdjournedKeys = []
    for x in range(0, len(population)):
        solution, fitness, element = decoderGreedyApproach(population[x])
        sortedPopulation.append([x, fitness])
        populationWithAdjournedKeys.append(element)
        listPosssibleBestSolution.append([solution, fitness])

    sortedPopulation = nonIncreasingOrder(sortedPopulation, 1)  # we order by fitness which is the second element
    listPosssibleBestSolution = nonIncreasingOrder(listPosssibleBestSolution, 1)

    return sortedPopulation, populationWithAdjournedKeys, listPosssibleBestSolution[0]


# check if the element is in the offspring already
def check(elem, offspring):
    for x in offspring:
        if elem in x: return True
    return False


# one element from the etilist set and one element from the remainder of the population ( P - {e} )
# same element can't be both parents
# don't check if the couple has been picked already, but with different probabilities could produce different elements
# shouls check that the offspring is not in the population already
def crossover(sortedPop, population, ne):
    offspring = []
    parentAindex = randint(0, ne)  # it doesn't take the right extremity
    parentBindex = randint(0, len(population))
    while (parentAindex == parentBindex):
        parentBindex = randint(0, len(population))
    parentA = population[sortedPop[parentAindex][0]]
    parentB = population[sortedPop[parentBindex][0]]

    bool = 0
    for x in range(0, len(parentA)):
        if len(parentA) != len(parentB):
            print(("different lenghts of parents !!! parentA: ", len(parentA), " parentB: ", len(parentB)))
        if (rand() <= P):  # parentA
            if offspring == []:
                offspring.append(parentA[x])
            else:
                flag = False
                while (flag == False):
                    # print("bool = ", bool)
                    if (bool / 2 == 0):  # parentA turn
                        if (check(parentA[x - int(bool / 2)][0], offspring)):
                            bool += 1
                        else:
                            offspring.append(parentA[x - int(bool / 2)])
                            bool = 0
                            flag = True
                    else:  # parentBturn
                        if (check(parentB[x - int(bool / 2)][0], offspring)):
                            bool += 1
                        else:
                            offspring.append(parentB[x - int(bool / 2)])
                            bool = 0
                            flag = True
        else:  # parentB
            if offspring == []:
                offspring.append(parentB[x])
            else:
                flag = False

                while (flag == False):
                    # print("bool = ", bool)
                    if (bool / 2 == 0):
                        if (check(parentB[x - int(bool / 2)][0], offspring)):
                            bool += 1
                        else:
                            offspring.append(parentB[x - int(bool / 2)])
                            bool = 0
                            flag = True
                    else:
                        if (check(parentA[x - int(bool / 2)][0], offspring)):
                            bool += 1
                        else:
                            offspring.append(parentA[x - int(bool / 2)])
                            bool = 0
                            flag = True

    return offspring


def newGeneration(population):
    newGeneration = []

    sortedPopulation, population, possibleBestSolution = sortPopulationByFitnessGreedy(population)

    bestFitness = sortedPopulation[0][1]

    nOfElite = int(len(population) * E)
    nOfRandom = int(len(population) * R)
    nOfCrossOver = len(population) - (nOfElite + nOfRandom)

    # copying the elite to the new generation
    for x in range(0, nOfElite):
        newGeneration.append(population[sortedPopulation[x][0]])
    for x in range(0, nOfRandom):
        newGeneration.append(createKeysForElement(len(bids)))

    # listOfPicked = np.zeros(len(bids))
    for x in range(0, nOfCrossOver):
        offSpring = crossover(sortedPopulation, population, nOfElite)
        while offSpring in newGeneration:
            offSpring = crossover(sortedPopulation, population, nOfElite)
            # print("same element")
        newGeneration.append(offSpring)

    return [newGeneration, bestFitness, possibleBestSolution]


def BRKGAGreedyApproach(populationSize):  # continua until the stopping criteria is not met
    population = createPopulation(populationSize)
    generationCount = 1
    bestFitness = 0
    fitnessNotIncreasingCount = 0
    bestSolutionSoFar = []
    while (fitnessNotIncreasingCount < 500 and generationCount < 1000):  # when one of the two finish
        population, generationBestFitness, possibleBestSolution = newGeneration(population)

        if bestSolutionSoFar == []:
            bestSolutionSoFar = possibleBestSolution
        else:
            if bestSolutionSoFar[1] < possibleBestSolution[1]:
                bestSolutionSoFar = possibleBestSolution
        if (bestFitness < generationBestFitness):
            bestFitness = generationBestFitness
            fitnessNotIncreasingCount = 0
        else:
            if (bestFitness == generationBestFitness):
                fitnessNotIncreasingCount += 1
            else:
                fitnessNotIncreasingCount += 1
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("the fitness decrease from: ", bestFitness, " to: ", generationBestFitness)

        print("BestFitness: ", bestFitness, " Genertion count: ", generationCount)
        # print(generationCount)
        generationCount += 1

    fitnessArray = printPopulation(population)
    printIndicesOfBidOfPopulation(population, fitnessArray)
    #decoding the fitness of the best solution found so far
    print(decoderForSolution(bestSolutionSoFar[0])[0])

    return int(0)



BRKGAGreedyApproach(10)
