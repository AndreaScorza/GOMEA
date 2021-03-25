'''import ast

biased = []
unbiased = []
lines = filter(None, (line.rstrip() for line in open("300L1-250-1000biased.txt")))
for line in lines:
    biased.append(ast.literal_eval(line))

lines = filter(None, (line.rstrip() for line in open("300L1-250-1000unbiased.txt")))
for line in lines:
    unbiased.append(ast.literal_eval(line))

print(biased)
print(unbiased)

import GOMEANormal as normal
import GOMEAUnivariate as univariate

tipe = "univariate"
#population, bestFit, time, val, foundAtGen, totFitEval, counter, improvement = normal.GOMEA(10, "L3-20-20.txt")
population, bestFit, time, val, totFotEval, foundAtGen, counter, improvement = univariate.GOMEA(10, "L3-20-20.txt")
x = [bestFit, foundAtGen, improvement, counter, round(time, 3)]

print(x)
print(type(univariate))'''
'''from numpy.random import randint
import random
import numpy as np
import linkageTree2 as lt
import orderingProblemValues as order

l = 8
k = 4


def createPop2(size):
    pop = []
    popByte = []
    block = [1, 2, 3, 4]
    for x in range(0, size):
        temp = []
        for y in range(0, l):
            temp.append(np.random.rand())
        pop.append(temp)
        individual = []
        for x in range(0, int(l / k)):
            #tail = random.sample(block, len(block))
            #individual = np.concatenate((individual, tail))
            individual = individual + random.sample(block, len(block))
            #individual.append(random.sample(block, len(block)))
        #popByte.append(list(np.hstack(individual)))
        popByte.append(individual)
    return pop, popByte


def createPop(size):
    pop = []
    popByte = []
    block = [1, 2, 3, 4]
    for x in range(0, size):
        temp = []
        for y in range(0, l):
            temp.append(np.random.rand())
        pop.append(temp)
        individual = []
        for x in range(0, int(l / k)):
            #tail = random.sample(block, len(block))
            #individual = np.concatenate((individual, tail))
            individual = individual + random.sample(block, len(block))
            #individual.append(random.sample(block, len(block)))
        #popByte.append(list(np.hstack(individual)))
        popByte.append(list(randint(2, size=l)))
        #popByte.append(individual)
    return pop, popByte


pop, popbyte = createPop(3)

for x in popbyte:
    print(len(x), type(x), x)
for x in pop:

    for y in range(0, len(x)):
        x[y] += 3
    print(len(x), type(x), x)



lT = lt.getLinkageTree(popbyte)
for x in lT:
    print(x)
'''

def test(input, type):
    if type == 'a':
        if input > 1:
            return 1
        return 0
    elif type == 'b':
        if input > 1:
            return 2
        return 0
    else:
        return 0

print(test(1, 'b'))
