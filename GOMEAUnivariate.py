import population as pop
import linkageTree as lt
import numpy as np
import decoder as dc
from numpy.random import randint
import time
import random
import statistics as stat

fitnessList = []

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
    index = population.index(sol)
    accepted = 0
    discarted = 0
    bestElem = sol.copy()
    for cluster in subset:
        solFit = fitnessList[index]
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
                fitnessList[index] = newSolFit
        else:
            discarted += 1
    #print("Accepted : ", accepted, " Discarted : ", discarted)
    return sol, bestFit, bestElem



def terminated(counter, notProgress):
    if counter > 30 or notProgress > 0:
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



def GOMEA(popSize, problem):
    counter = 0
    startTime = time.time()
    #  values = [goodsNumber, bidsNumber, dummyNumber, bidsValue, bids]
    population, values = pop.population(popSize, problem, -1)

    for x in population:
        fitnessList.append(dc.getFitness(x, values[3], values[1], values[4]))


    bestFit = 0
    bestElem = []
    stationaryCounter = 0
    #printStat(population, values)
    notProgress = 0

    # --
    flag = False
    foundAtGen = 0
    subset = []
    for y in range(0, len(population[0])):
        subset.append([y])
    while not terminated(counter, notProgress):
        lastRoundPopulation = population.copy()
        for x in range(0, len(population)):
            donor = getDonor(population, x)
            population[x], fit, elem = greedyRecomb(population[x], donor, subset, values, population)
            if bestFit < fit:
                bestFit = fit
                stationaryCounter = 0
                foundAtGen = counter + 1
        stationaryCounter += 1

        if counter == 0:
            #print("fit", bestFit)
            initialFitness = bestFit
        counter += 1

        # --


        #print(counter, " : ", bestFit)
        numberOfChange = howManyOfThePopChanged(lastRoundPopulation, population)
        if numberOfChange == 0:
            notProgress += 1
        else:
            notProgress = 0
        #print(numberOfChange, " elements have changed since last generation")

        #printStat(population, values)

        '''if bestFit > 48932.8 and flag == False:
            foundAtGen = counter
            print("ora esce")
            break'''
    return population, bestFit, time.time() - startTime, values, foundAtGen, counter,  round(bestFit - initialFitness, 5)
'''
fitList = []
genList = []
improvementList = []
for x in range(0, 1):
    population, bestFit, val, foundAtGen, counter, improvement = GOMEA(10, "L3-20-20.txt")
    print("best fit", bestFit, " found at gen: ", foundAtGen, " Fitness improved of: ", improvement)
    fitList.append(bestFit)
    genList.append(foundAtGen)
    improvementList.append(improvement)

for x in range(0, len(genList)):
    print(fitList[x], " ", genList[x])

print("average best fitness: ", stat.mean(fitList))
print("median best fitness: ", stat.median(fitList))
try:
    print("mode best fitness: ", stat.mode(fitList))
except:
    print(("mode best fitness:     All values are different"))

print("average found at gen: ", stat.mean(genList))
print("median found at gen: ", stat.median(genList))
try:
    print("mode found at gen: ", stat.mode(genList))
except:
    print("mode found at gen:     All values are different")
print("average improvement: ", stat.mean(improvementList))
print("median improvement: ", stat.median(improvementList))
try:
    print("mode improvement: ", stat.mode(improvementList))
except:
    print("mode improvement:     All values are different")'''


