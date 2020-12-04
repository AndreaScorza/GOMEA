import population as pop
import linkageTree as lt
import numpy as np
import decoder as dc
from numpy.random import randint

#  values = [goodsNumber, bidsNumber, dummyNumber, bidsValue, bids]
population, values = pop.population(10, "L4-5-5.txt", -1)


'''for x in population:
    print(x)'''

lT = lt.getLinkageTree(population)

def getDonor(population):
    donorIndex = randint(0, len(population))  # excluded the right extremity of the interval
    #print(donorIndex)
    return population[donorIndex]

def greedyRecomb(sol, donor, subset, population):
    for cluster in subset:
        print("new cluster")
        for element in cluster:
            print(element)

for subset in lT:
    # controlla che il donor non sia lo stesso dell'elemento della popolazione
    donor = getDonor(population)
    sol = population[0]
    # qua ci sarà la funzione e la greedy verra chiamata direttamente con popolazione di [x]

#greedyRecomb(population[0], population[1], lT[1], population)
fitness = dc.getFitness(population[0], values[3], values[1], values[4])

