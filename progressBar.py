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
print(unbiased)'''

import GOMEANormal as normal
import GOMEAUnivariate as univariate

#population, bestFit, time, val, foundAtGen, totFitEval, counter, improvement = normal.GOMEA(10, "L3-20-20.txt")
population, bestFit, time, val, foundAtGen, counter, improvement = univariate.GOMEA(10, "L3-20-20.txt")
x = [bestFit, foundAtGen, improvement, counter, round(time, 3)]

print(x)

