'''# beginning of comparison or adjacency matrix based with our without BRK encoding

import numpy as np
import linkageTree as lt
import time
from numpy.random import randint
import random

# global variable
k = 2
l = 6
import seed
#byteArray = np.random.randint(2, size=l)

def createPop(size):
    pop = []
    popByte = []
    for x in range(0, size):
        temp = []
        for y in range(0, l):
            temp.append(np.random.rand())
        pop.append(temp)
        popByte.append(list(randint(2, size=l)))
    return pop, popByte

pop, popByte = createPop(100)
lT = lt.getLinkageTree(pop)
for x in lT:
    print(x)
lT2 = lt.getLinkageTree(popByte)
print("\n")
for x in lT2:
    print(x)
lT3 = lt.getLinkageTree(popByte)
print("\n")
for x in lT3:
    print(x)
'''
from scipy import stats
import statistics as stat

arr1 = [2,3,4,2,3,4,2,3,4]
arr2 = [4,5,6,5,4,6,4,5,6]
print(stat.variance(arr1))
print(stat.variance(arr2))
print(stats.ttest_ind(arr2, arr1))