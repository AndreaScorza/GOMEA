# The problem in the C code is at the function at line 932
# void initializeNewGOMEAMemory() sometimes it finishes sometimes it throws an exception

import population as pop
import numpy as np
import math
from numpy.random import randint
import random
from numpy import interp

# this version of the linkage tree is created for the deceptive problems, when there random keys are not used
# the second delta needs a value in [0,1] interval but the values ranges from 0 to 4 for the deceptive problem
# hence to calculate the second delta we must map the values to the 0,1 interval

# we want the probability than integer i before integer j

def createDependencyMatrix(population):
    # create the matrix
    dependencyMatrix = np.zeros((len(population[0]), len(population[0])))

    nBids = len(population[0])
    #print("nbids ", nBids)
    for i in range(0, nBids):
        for j in range(i + 1, nBids):
            p = 0
            for k in range(0, len(population)):
                # here we have the problem
                # < OR > doesn't change the result
                if population[k][i] < population[k][j]:
                    p += 1
            p /= len(population)
            # is this condition true ? yes : no
            # (p==0)||(p==1)?0:-(p*log2(p) + (1.0-p)*log2(1.0-p));
            if p == 0 or p == 1:
                #print("this case")
                entropy = 0
            else:
                entropy = -(p*(math.log(p, 2)) + (1.0-p)*(math.log((1.0-p), 2)))
            dependencyMatrix[i][j] = 1 - entropy
            # now we multiply by the inverted average distance between variables (delta2)
            averageDistance = 0
            for k in range(0, len(population)):
                # changing the values interval from 0,4 to 0,1
                averageDistance += pow((interp(population[k][i],[0,4],[0,1]) - interp(population[k][j],[0,4],[0,1])), 2)
            averageDistance /= len(population)
            #To just use delta 1 comment the following line
            dependencyMatrix[i][j] *= 1 - averageDistance
            # To just use delta 2 uncomment the following line and comment the one above
            #dependencyMatrix[i][j] = 1 - averageDistance
            # ------ end of delta 2
            # creating the symmetric matrix
            # --- trying a random int, 0 or 1
            #dependencyMatrix[i][j] = randint(2)

            # --- or a real number between 0 and 1
            #dependencyMatrix[i][j] = random.uniform(0,1)


            dependencyMatrix[j][i] = dependencyMatrix[i][j]
    zeroCount = 0
    for x in range(0, len(dependencyMatrix)):
        for j in range(0, len(dependencyMatrix)):
            if dependencyMatrix[x][j] == 0:
                zeroCount += 1
    #print("Zero count of dependency matrix is : ", zeroCount, " len: ", len(dependencyMatrix))
    #print("\n", dependencyMatrix)
    return dependencyMatrix


# get the dependency between two clusters based on the matrix
def clustersDependencies(list1, list2, matrix):
    cont = 0
    sum = 0
    for x in list1:
        for y in list2:
            cont += 1
            sum += matrix[x][y]
    return sum/cont

# return the dependencies for each element/cluster of the branch
def getDependenciesForBranch(dependencyMatrix, branch):
    dependency = []
    for i in range(0, len(branch)):
        dep = 0
        stored = []
        for j in range(0, len(branch)):
            if j != i:
                x = clustersDependencies(branch[i], branch[j], dependencyMatrix)
                if x == dep:
                    stored.append(j)
                if x > dep:
                    dep = x
                    stored = [j]

        dependency.append(stored)
    return dependency

def isInList(elem, list):
    if list == []:
        return False
    else:
        if isinstance(list, int):
            if list == elem:
                return True
            else:
                return False
        else:
            for x in range(0, len(list)):
                if isinstance(list[x], int):
                    if elem == list[x]:
                        return True
                else:
                    for y in range(0, len(list[x])):
                        if elem == list[x][y]:
                            return True
            return False

# translate the dependency from a list of indexes to their actual value
def translateDependency(branch, dependency):
    newDep = []
    for x in range(0, len(dependency)):
        newDep.append(branch[dependency[x][0]])
    return newDep

# based on the branch and the dependecy, it creates the next branch
def createNextBranch(branch, dependency):
    dependency = translateDependency(branch, dependency)
    nextBranch = []
    for x in range(0, len(branch)):
        new = []
        for z in range(0, len(branch[x])):
            if not isInList(branch[x][z], nextBranch):
                toAdd = []
                for y in dependency[x]:
                    if not isInList(y, nextBranch):
                        toAdd.append(y)
                if toAdd != []:
                    for j in branch[x]:
                        new.append(j)
                    if isinstance(toAdd, int):
                        new.append(toAdd)
                    else:
                        for j in toAdd:
                            new.append(j)
                    nextBranch.append(new)
    return nextBranch

# it returns the branch with the single element that were not included in any clusters
# it is needed to calculate the dependencies (since a branch doesn't necessary contains all the variables)
def branchWithUnary(oldbranch, newbranch):
    unaryBranch = newbranch.copy()
    for x in oldbranch:
        for y in x:
            flag = False
            if isInList(y, newbranch):
                flag = True
        if flag == False:
            unaryBranch.append(x)
    return unaryBranch



def getUnivariateAndRoot(population):
    univariate = []
    root = []
    for x in range(0, len(population[0])):
        univariate.append([x])
        root.append(x)


    return univariate, [root]

# check if the univariate is the same of the root, undependently of the order of the element
def rootSameUni(root, univariate):
    univ = univariate.copy()
    univ[0].sort()
    return univ == root

def getLinkageTree(population):
    tree = []
    univariate, root = getUnivariateAndRoot(population)
    unaryBranch = univariate.copy()
    tree.append(unaryBranch)
    dependencyMatrix = createDependencyMatrix(population)
    while not rootSameUni(root, unaryBranch):
        dependencies = getDependenciesForBranch(dependencyMatrix, unaryBranch)
        nextBranch = createNextBranch(unaryBranch, dependencies)
        tree.append(nextBranch)
        unaryBranch = branchWithUnary(unaryBranch, nextBranch)
    return tree

'''population, val = pop.population(10, "L3-20-20.txt", -1)
tree = getLinkageTree(population)
for x in range(0, len(tree[:-1])):
    print (x, tree[x])'''

