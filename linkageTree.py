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




# parameters (population size, file, and seed() )
population = pop.population(5, "L4-5-5.txt", 1)
dependencyMatrix = createDependencyMatrix(population)

branch = [[0],[1],[2],[3],[4]]
dependencyMatrix[0][1] = dependencyMatrix[0][2]
print(dependencyMatrix)

branchDep = getDependenciesFromBranch(dependencyMatrix, branch)
print(branchDep)

print(clustersDependencies([0,1], [2, 3] , dependencyMatrix))

