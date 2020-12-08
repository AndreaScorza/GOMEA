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

def checkIfElemInPopulation(elem, pop):
    if pop == []:
        return False
    else:
        for x in range(0, len(pop)):
            if elem == pop[x]:
                print("The element created initially was already present, discarted")
                return True
        return False


# create the population from the random keys of defined size
def createPopulation(size, values):
    population = []
    for elem in range(0, size):
        newElem = createKeysForElement(len(values[4]))
        while(checkIfElemInPopulation(newElem, population)):
            newElem = createKeysForElement(len(values[4]))
        population.append(newElem)
        print(elem)
        #population.append(createKeysForElement(len(values[4])))
    return population, values


def population(size, filename, sEed):
    if sEed >= 0:
        seed(sEed)
    values = auction.getAuction(filename)
    return createPopulation(size, values)

