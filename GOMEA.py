import population as pop
import linkageTree as lt
import numpy as np
import decoder as dc
from numpy.random import randint
import time
import random

def getDonor(population, x):
    numbers = list(range(0, len(population)))
    numbers.remove(x)
    donorIndex = random.choice(numbers)  # excluded the right extremity of the interval
    return population[donorIndex]


def secondCheck(element, population, val):
    useless, elemSol = dc.getFitnessAndStats(element, val[3], val[1], val[4])
    elemSol.sort()
    for x in population:
        fit, stat = dc.getFitnessAndStats(x, val[3], val[1], val[4])
        stat.sort()
        if stat == elemSol:
            return False
    return True

def greedyRecomb(sol, donor, subset, values, population, forcedImprovement, superiorDonor):
    accepted = 0
    discarted = 0
    bestElem = sol.copy()
    for cluster in subset:
        solFit = dc.getFitness(sol, values[3], values[1], values[4])
        newSol = sol.copy()
        for element in cluster:
            if not forcedImprovement:
                newSol[element] = donor[element]
            else:
                newSol[element] = superiorDonor[element]
        newSolFit = dc.getFitness(newSol, values[3], values[1], values[4])
        bestFit = solFit

    #    print(howManyOfThePopChanged(sol, newSol))
    #    print(newSolFit, " new")
        if newSolFit > solFit:
            accepted += 1
            # we add a second check to see if the solution resulting would be the same, we discarted because same element
            #if not pop.checkIfElemInPopulation(newSol, population):
            if not pop.checkIfElemInPopulation(newSol, population) and secondCheck(newSol, population, values):
                sol = newSol
                bestFit = newSolFit
                bestElem = newSol.copy()
        else:
            discarted += 1
    #print("Accepted : ", accepted, " Discarted : ", discarted)
    return sol, bestFit, bestElem



def terminated(counter, notProgress):
    if counter > 100 or notProgress > 1:
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

def printStat(population, val):
    # [goodsNumber, bidsNumber, dummyNumber, bidsValue, bids]
    for x in population:
        fit, stat = dc.getFitnessAndStats(x, val[3], val[1], val[4])
        print(round(fit, 2), " ", x, " ", stat)



def GOMEA():
    forcedImprovement = False
    startTime = time.time()
    counter = 0
    #  values = [goodsNumber, bidsNumber, dummyNumber, bidsValue, bids]
    #population, values = pop.population(10, "L3-20-20.txt", -1)
    population, values = pop.population(10, "problemInstances/matching.txt", -1)
    bestFit = 0
    bestElem = []
    stationaryCounter = 0
    printStat(population, values)
    notProgress = 0

    # --
    flag = False
    trovato = 0

    while not terminated(counter, notProgress):
        # uncomment for forcer improvmenet
        #if stationaryCounter > 6:
        #    forcedImprovement = True
        #    print("Forced improvement !!!!!!!!!!!!!!!!!")
        lastRoundPopulation = population.copy()

        # ----------------

        lT = lt.getLinkageTree(population)

        # to create the random linkage tree comment up and uncomment down:
        #a, b = pop.population(10, "L3-20-20.txt", -1)
        #lT = lt.getLinkageTree(a)
        # -----------------

        for li in lT[:-1]:
            print(li)
        for x in range(0, len(population)):
            for subset in lT[:-1]:  # avoiding the root of the tree
                donor = getDonor(population, x)
                population[x], fit, elem = greedyRecomb(population[x], donor, subset, values, population, forcedImprovement, bestElem)
                if bestFit < fit:
                    bestFit = fit
                    bestElem = elem.copy()
                    stationaryCounter = 0
        stationaryCounter += 1
        counter += 1

        # --
        if bestFit > 3082.75 and flag == False:
            trovato = counter
            flag = True

        print(counter, " : ", bestFit, " time: ", round(time.time() - startTime, 2))
        numberOfChange = howManyOfThePopChanged(lastRoundPopulation, population)
        if numberOfChange == 0:
            notProgress += 1
        else:
            notProgress = 0
        print(numberOfChange, " elements have changed since last generation")

        printStat(population, values)
    return population, bestFit, time.time() - startTime, values
    #return population, bestFit, time.time() - startTime, values, trovato, counter


population, bestFit, time, val = GOMEA()

print(bestFit, " : ", round(time, 2))
print()
#  controlli sulla popolazione:

for x in population:
    print(dc.getFitness(x, val[3], val[1], val[4]))#, " : ", x)

for x in range(0, len(population) - 1):
    for j in range(x + 1, len(population)):
        if population[x] == population[j]:
            print("are the same")



'''store = []
for x in range(0, 3):
    popol, bestFit, val, trovato, counter = GOMEA()
    Flag = True
    for x in popol:
        if round(dc.getFitness(x, val[3], val[1], val[4]), 2) != 3082.78:
            Flag = False
            break
    store.append([counter, trovato, Flag])
for x in store:
    print (x)'''

