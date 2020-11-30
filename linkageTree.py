# The problem in the C code is at the function at line 932
# void initializeNewGOMEAMemory() sometimes it finishes sometimes it throws an exception

import population as pop
import numpy as np
import math


# we want the probability than integer i before integer j

def createDependencyMatrix(population):
    # create the matrix
    dependencyMatrix = np.zeros((len(population[0]), len(population[0])))

    nBids = len(population[0])
    for i in range(0, nBids):
        for j in range(i + 1, nBids):
            p = 0
            for k in range(0, len(population)):
                if population[k][i] < population[k][j]:
                    p += 1
            p /= len(population)
            # is this condition true ? yes : no
            # (p==0)||(p==1)?0:-(p*log2(p) + (1.0-p)*log2(1.0-p));
            if p == 0 or p == 1:
                print("this case")
                entropy = 0
            else:
                entropy = -(p*(math.log(p, 2)) + (1.0-p)*(math.log((1.0-p), 2)))
            dependencyMatrix[i][j] = 1 - entropy
            # now we multiply by the inverted average distance between variables (delta2)
            averageDistance = 0
            for k in range(0, len(population)):
                averageDistance += (population[k][i] - population[k][j]) * (population[k][i] - population[k][j])
            averageDistance /= len(population)
            dependencyMatrix[i][j] *= 1 - averageDistance

            # creating the symmetric matrix
            dependencyMatrix[j][i] = dependencyMatrix[i][j]

    return dependencyMatrix


# compare dependencies between cluster and cluster
def clustersDependencies(list1, list2, matrix):
    cont = 0
    sum = 0
    for x in list1:
        for y in list2:
            cont += 1
            sum += matrix[x][y]
    return sum/cont


def getDependenciesFromBranch(dependencyMatrix, branch):
    dependency = []
    for i in range(0, len(branch)):
        dep = 0
        for j in range(0, len(branch)):
            if j != i:
                x = clustersDependencies(branch[i], branch[j], dependencyMatrix)
                if x == dep:
                    # stored.append([dep, j])
                    stored.append(j)
                if x > dep:
                    dep = x
                    stored = [j]
                    # stored.append([dep, j])

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


def createNextBranch(branch, dependency):
    nextBranch = []
    for x in range(0, len(branch)):
        if not isInList(branch[x][0], nextBranch): # !!!! controlla che next branch è [[1, 3] , [2,4]] c'è non è una lista di elementi ma una lista di liste
            toAdd = []
            for y in dependency[x]:
                if not isInList(y, nextBranch):
                    toAdd.append(y)
            if toAdd != []:
                new = []
                new.append(branch[x][0])
                if isinstance(toAdd, int):
                    new.append(toAdd)
                else:
                    for j in toAdd:
                        new.append(j)
                nextBranch.append(new)
    return nextBranch

# it returns the branch with the single element that were not included in the cluster
# it is needed to calculate the dependencies (since a branch doesn't necessary contains all the variables)
def branchWithUnary(oldbranch, newbranch):
    toAdd = []
    unaryBranch = newbranch.copy()
    for x in oldbranch:
        for y in x:
            if not isInList(y, newbranch):
                unaryBranch.append([y])
    return unaryBranch

# parameters (population size, file, and seed() )
population = pop.population(5, "L4-5-5.txt", 1)
dependencyMatrix = createDependencyMatrix(population)

branch = [[0],[1],[2],[3],[4]]
dependencyMatrix[0][1] = dependencyMatrix[0][2]
print(dependencyMatrix)

branchDep = getDependenciesFromBranch(dependencyMatrix, branch)
print(branch)
#branchDep[3] = [4]
print(branchDep)

# from the branch and the branch dependencies it returns the next branch
nextBranch = createNextBranch(branch, branchDep)


print("next", nextBranch)
print(branchWithUnary(branch, nextBranch))