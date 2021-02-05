import population as pop
import linkageTree as lt
import numpy as np
import decoder as dc
from numpy.random import randint
import time
import random
import statistics as stat

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

def greedyRecomb(sol, donor, subset, values, population):
    accepted = 0
    discarted = 0
    bestElem = sol.copy()
    for cluster in subset:
        solFit = dc.getFitness(sol, values[3], values[1], values[4])
        newSol = sol.copy()
        for element in cluster:
            newSol[element] = donor[element]
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
    if counter > 30 or notProgress > 1:
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
    counter = 0
    #  values = [goodsNumber, bidsNumber, dummyNumber, bidsValue, bids]
    population, values = pop.population(20, "L2-50-100.txt", -1)
    bestFit = 0
    bestElem = []
    stationaryCounter = 0
    #printStat(population, values)
    notProgress = 0

    # --
    flag = False
    foundAtGen = 0

    while not terminated(counter, notProgress):
        lastRoundPopulation = population.copy()

        # ----------------

        lT = lt.getLinkageTree(population)

        # to create the random linkage tree comment up and uncomment down:
        #a, b = pop.population(10, "L3-20-20.txt", -1)
        #lT = lt.getLinkageTree(a)
        # -----------------

        for x in range(0, len(population)):
            for subset in lT[:-1]:  # avoiding the root of the tree
                donor = getDonor(population, x)
                population[x], fit, elem = greedyRecomb(population[x], donor, subset, values, population)
                if bestFit < fit:
                    bestFit = fit
                    bestElem = elem.copy()
                    stationaryCounter = 0
                    foundAtGen = counter + 1
        stationaryCounter += 1
        if counter == 0:
            print("fit", bestFit)
            initialFitness = bestFit
        counter += 1

        # --


        print(counter, " : ", bestFit)
        #numberOfChange = howManyOfThePopChanged(lastRoundPopulation, population)
        #if numberOfChange == 0:
        #    notProgress += 1
        #else:
        #    notProgress = 0
        #print(numberOfChange, " elements have changed since last generation")

        #printStat(population, values)

        if bestFit > 48932.8 and flag == False:
            foundAtGen = counter
            print("ora esce")
            break
    return population, bestFit, values, foundAtGen, counter, bestFit - initialFitness

fitList = []
genList = []
improvementList = []
for x in range(0, 3):
    population, bestFit, val, foundAtGen, counter, improvement = GOMEA()
    print("best fit", bestFit, " found at gen: ", foundAtGen, " Fitness improved of: ", improvement)
    fitList.append(bestFit)
    genList.append(foundAtGen)
    improvementList.append(improvement)

print("\n")
for x in range(0, len(genList)):
    print(fitList[x], " ", genList[x])

print("\n")
print("average best fitness: ", stat.mean(fitList))
print("median best fitness: ", stat.median(fitList))
try:
    print("mode best fitness: ", stat.mode(fitList))
except:
    print(("mode best fitness:     All values are different"))

print("\n")
print("average found at gen: ", stat.mean(genList))
print("median found at gen: ", stat.median(genList))
try:
    print("mode found at gen: ", stat.mode(genList))
except:
    print("mode found at gen:     All values are different")
print("\n")
print("average improvement: ", stat.mean(improvementList))
print("median improvement: ", stat.median(improvementList))
try:
    print("mode improvement: ", stat.mode(improvementList))
except:
    print("mode improvement:     All values are different")



