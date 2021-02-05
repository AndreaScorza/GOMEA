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

x = 20
subset = []
for y in range(0, x):
    subset.append([y])
print(subset)