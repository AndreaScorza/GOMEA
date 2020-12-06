import population as pop
import linkageTree as lt
import numpy as np
import decoder as dc
from numpy.random import randint
from tqdm import tqdm
import time


def getDonor(population):
    donorIndex = randint(0, len(population))  # excluded the right extremity of the interval
    #print(donorIndex)
    return population[donorIndex]

def greedyRecomb(sol, donor, subset, values):

    for cluster in subset:
        #print(cluster)
        for element in cluster:
            #print(element)
            solFit = dc.getFitness(sol, values[3], values[1], values[4])
            newSol = sol.copy()
            newSol[element] = donor[element]
            newSolFit = dc.getFitness(newSol, values[3], values[1], values[4])
            bestFit = solFit
            if newSolFit > solFit:
                sol = newSol
                bestFit = newSolFit
                '''print("sol", sol)
                print("new", newSol)
                print("solFit", solFit)
                print("newFit", newSolFit)'''
    return sol, solFit

def terminated(counter):
    if counter >= 10:
        return True
    return False

def GOMEA():
    startTime = time.time()
    #pbar = tqdm(total=10)
    counter = 0
    #  values = [goodsNumber, bidsNumber, dummyNumber, bidsValue, bids]
    population, values = pop.population(10, "L3-20-20.txt", -1)
    bestFit = 0
    while not terminated(counter):
        lT = lt.getLinkageTree(population)
        for sol in population:
            for subset in lT:
                donor = getDonor(population)
                while donor == sol:
                    donor = getDonor(population)
                #  this is used to check if sol have changed
                #a = sol.copy()
                sol, fit = greedyRecomb(sol, donor, subset, values)
                if bestFit < fit:
                    bestFit = fit
                '''if sol != a:
                    print("sol had changed")'''
        counter += 1
        #pbar.update(1)
        print(bestFit, " time: ", round(time.time()-startTime, 2))
    #pbar.close()
    return bestFit, round(time.time()-startTime, 2)


print(GOMEA())