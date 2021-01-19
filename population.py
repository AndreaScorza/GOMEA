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
        #  this check might be avoided in order to speed up the program, it is really rare
        while(checkIfElemInPopulation(newElem, population)):
            newElem = createKeysForElement(len(values[4]))
            print("the new element was already present in the population! creating a new one ...")
        population.append(newElem)
        #population.append(createKeysForElement(len(values[4])))
    return population, values


def population(size, filename, sEed):
    if sEed >= 0:
        seed(sEed)
    values = auction.getAuction(filename)
    return createPopulation(size, values)

pop, val = population(2, "L4-5-5.txt", -1)
for x in pop:
    print(x)
for x in val:
    print(x)
#[goodsNumber, bidsNumber, dummyNumber, bidsValue, bids]
'''print(len(val[3]))
print(len(val[4]))'''