from numpy.random import seed
from numpy.random import randint
from numpy.random import rand
import numpy as np
import inputBids as auction
import math

seed(1)

values = auction.getAuction('L4-5-5.txt')
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


# it is calculating the matrix for one element
# we utilize > instead of < since the BRKGA use decreasing order
def matrixForOneElement(element):
    n = len(element)
    matrix = np.zeros((n, n))
    for x in range(0, n):
        for y in range(0, n):
            if element[x][1] > element[y][1]:
                matrix[x][y] = + 1
    return matrix


def delta(p):
    if p == 0 or p == 1:
        return 1
    else:
        a = p * math.log(p, 2)
        b = (1 - p) * math.log((1 - p), 2)
        return 1 + (a + b)

# apply the delta to the all matrix
def deltaOne(matrix):
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix)):
            if (matrix[x][y]) != 0:
                matrix[x][y] = delta(matrix[x][y])
    return matrix

def matrixForThePopulation(population):
    n = len(population[0])
    matrix = np.zeros((n, n))
    for element in population:
        matrix += matrixForOneElement(element)
    print(matrix)
    print(" ")
    matrix = matrix * (1 / n)
    print(matrix)
    print(" ")
    matrix = deltaOne(matrix)
    print(matrix)
    print(" ")
    return matrix
    #return deltaOne(matrix * (1 / n))

def neighbourList(matrix, structure, branch):
    if sum(structure) == 0: # univariate case
        cluster = []
        distanceList = []
        neighbourList = []
        for x in range(0, len(matrix)):
            distance = 2
            neighbour = []
            for y in range(0, len(matrix)):
                if matrix[x][y] != 0 and matrix[x][y] < distance:
                    distance = matrix[x][y]
                    neighbour = []
                    neighbour.append([x, y])
                else:
                    if matrix[x][y] != 0 and matrix[x][y] == distance:
                        neighbour.append([x, y])
            distanceList.append(distance)
            neighbourList.append(neighbour)

        return distanceList, neighbourList, cluster
    else:

        notInBranch = []
        for x in range(0, len(structure)):
            if structure[x] == 0:
                notInBranch.append(x)
        #print(notInBranch)
        branch.append(notInBranch)
        print(branch)
        #for x in branch:

        return int(0), 0, 0



# from the neighbour list and the univariate create the first branch
def fromUnivariateToFirstBranch(structure, neighbour):

    final = neighbour.copy()
    toRemove = [] # list of indices of elements to remove
    for x in neighbour:
        if len(x) == 1: # it has one parenthesis more
            flag = False
            for y in x[0]:
                if structure[y] != 0:
                    flag = True
            if flag:
                toRemove.append(x)
            else:
                for y in x[0]:
                    structure[y] = 1
        else:
            for y in x:
                flag = False
                for every in y:
                    if structure[every] != 0:
                        flag = True
                if flag:
                    toRemove.append(y)
                else:
                    for every in y:
                        structure[every] = 1
    for x in range(0, len(toRemove)):
        if len(toRemove[x]) == 1:
            toRemove[x] = toRemove[x][0]
    secondFinal = []
    for x in range(0, len(final)):
        for y in final[x]:
            secondFinal.append(y)
    for x in toRemove:
        secondFinal.remove(x)
    return structure, secondFinal




# inizia qui
population = createPopulation(6)

matrix = matrixForThePopulation(population)


structure = np.zeros(len(matrix))
dist, neighbour, cluster = neighbourList(matrix, structure, 0) # first time it should be the univariate
print("neighbour ",neighbour)
structure, firstBranch = fromUnivariateToFirstBranch(structure, neighbour)
print(structure, " --- ", firstBranch)
dist, neighbour, cluster = neighbourList(matrix, structure, firstBranch) # first time it should be the univariate


