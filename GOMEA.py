import population as pop
import linkageTree as lt
import numpy as np
import decoder as dc
from numpy.random import randint
import time


def getDonor(population):
    donorIndex = randint(0, len(population))  # excluded the right extremity of the interval
    # print(donorIndex)
    return population[donorIndex]


def greedyRecomb(sol, donor, subset, values, population):
    for cluster in subset:
        for element in cluster:
            solFit = dc.getFitness(sol, values[3], values[1], values[4])
            newSol = sol.copy()
            newSol[element] = donor[element]
            newSolFit = dc.getFitness(newSol, values[3], values[1], values[4])
            bestFit = solFit
            if newSolFit > solFit:
                if not pop.checkIfElemInPopulation(newSol, population):
                    sol = newSol
                    bestFit = newSolFit
                else:
                    print("The solution was already present in the population, hence discarted")

    return sol, bestFit


def terminated(counter):
    if counter > 10:
        return True
    return False


#  those are all checking functions --------------
def solInPop(sol, pop):
    for x in pop:
        if sol == x:
            print("trovato")
            print(x)
            print(sol)

#  count how many elements changed from two populations
def howManyOfThePopChanged(pop, newPop):
    number = 0
    for x in range(0, len(pop)):
        if pop[x] != newPop[x]:
            number += 1
    return number

#  ----------------------------------------------


def GOMEA():
    startTime = time.time()
    counter = 0
    #  values = [goodsNumber, bidsNumber, dummyNumber, bidsValue, bids]
    population, values = pop.population(10, "L3-20-20.txt", -1)

    # this is just for checking
    initialPopulation = population.copy()
    bestFit = 0
    while not terminated(counter):
        lastRoundPopulation = population.copy()
        lT = lt.getLinkageTree(population)
        for y in range(0, len(population)):
            print(dc.getFitness(population[y], values[3], values[1], values[4]))
        for x in range(0, len(population)):
            for subset in lT:
                donor = getDonor(population)
                while donor == population[x]:
                    donor = getDonor(population)
                population[x], fit = greedyRecomb(population[x], donor, subset, values, population)
                if bestFit < fit:
                    bestFit = fit

        counter += 1
        print(counter, " : ", bestFit, " time: ", round(time.time() - startTime, 2))
        print(howManyOfThePopChanged(initialPopulation, population), " elements have changed from the initial population")
        print(howManyOfThePopChanged(lastRoundPopulation, population), " elements have changed since last generation")
    return population, bestFit, time.time() - startTime, values
    #return population, bestFit, time.time() - startTime


pop, bestFit, time, val = GOMEA()

print(bestFit, " : ", round(time, 2))


#  controlli sulla popolazione:

for x in pop:
    print(dc.getFitness(x, val[3], val[1], val[4]), " : ", x)


for x in range(0, len(pop)-1):
    for j in range(x+1, len(pop)):
        if pop[x] == pop[j]:
            print("are the same")
        else:
            print(x, " : ", j)
