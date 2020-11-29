from numpy.random import rand
import inputBids as auction
from numpy.random import seed



# create a double array of [indices, float[0,1] ]
def createKeysForElement(dimension):
    keys = []
    for x in range(0, dimension):
        #keys.append([x, float(rand())])
        keys.append(float(rand()))
    return keys


# create the population from the random keys of defined size
def createPopulation(size, bids):
    population = []
    for elem in range(0, size):
        population.append(createKeysForElement(len(bids)))
    return population


def population(size, filename, sEed):
    if sEed >= 0:
        seed(sEed)
    values = auction.getAuction(filename)
    bids = values[4]
    return createPopulation(size, bids)

