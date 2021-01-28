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

res = [[42110.92652000001, 1056],
[43204.8583, 2625],
[43403.205, 267],
[41432.00860000001, 861],
[40920.147200000014, 608],
[44723.68410000002, 1757],
[44756.084099999985, 914],
[41617.5273, 691],
[43435.706300000005, 991],
[40941.59010000001, 365],
[42549.0759, 1230],
[43700.88779999999, 1659],
[40239.41560000001, 662],
[44265.04730000002, 840],
[43986.29390000002, 1553],
[42112.66502000001, 1073],
[42852.16632000001, 640],
[42591.05380000001, 1014],
[43391.17660000001, 1817],
[41195.5479, 108]]
a = 0
b = 0
for x in res:
    a += x[0]
    b += x[1]
print(a/len(res), " ", b/len(res))