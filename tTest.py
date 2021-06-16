import BRKGAfinalChromo as BRKGA
import UnbiasedRKGAChromo as RKGA
import statistics as stat
from scipy import stats
import ast


def performStat(fit, gen):
    print("\nFitness: ")
    print("Average: ", stat.mean(fit))
    print("Median:  ", stat.median(fit))
    try:
        print("Mode:    ", stat.mode(fit))
    except:
        print(("Mode:     All values are different"))
    try:
        print("Variance:", stat.variance(fit))
    except:
        print(("Variance: Requires at least two data points"))
    print("St Dev:  ", stat.stdev(fit))

    print("\nGeneration: ")
    print("Average: ", stat.mean(gen))
    print("Median:  ", stat.median(gen))
    try:
        print("Mode:    ", stat.mode(gen))
    except:
        print(("Mode:     All values are different"))
    try:
        print("Variance:", stat.variance(gen))
    except:
        print(("Variance: Requires at least two data points"))
    print("St Dev:  ", stat.stdev(gen))


def performTTest(arr1, arr2, name):
    print(name, " ", stats.ttest_ind(arr1, arr2))


def performWilcoxon(arr1, arr2, name):
    try:
        print(name, " ", stats.wilcoxon(arr1, arr2))
    except:
        print("All elements are the same")

def readFromDataset(name):
    fit = []
    gen = []
    lines = filter(None, (line.rstrip() for line in open(name)))
    for line in lines:
        fit.append(ast.literal_eval(line)[0])
        gen.append(ast.literal_eval(line)[1])


    return fit, gen

'''problem = 'L3-20-20.txt'
Bfit, Bgen = BRKGA.runWithStatistics(10, 10, problem)
Ufit, Ugen = RKGA.runWithStatistics(10, 10, problem)'''


Bfit, Bgen = readFromDataset("Datasets/300L1-250-1000biased.txt")
Ufit, Ugen = readFromDataset("Datasets/300L1-250-1000unbiased.txt")

#Bfit, Bgen = readFromDataset("1000L6biased.txt")
#Ufit, Ugen = readFromDataset("1000L6unbiased.txt")
print("\n")
print("BRKGA best individual: ",max(Bfit))
print("RKGA best individual: ",max(Ufit))
# To make the datasets the same length
if len(Bfit) != len(Ufit):
    while (len(Bfit) < len(Ufit)):
        Ufit.pop()
        Ugen.pop()
    while (len(Bfit) > len(Ufit)):
        Bfit.pop()
        Bgen.pop()



print("\n")
print("BRKGA")
performStat(Bfit, Bgen)
print("\n")
print("RKGA")
performStat(Ufit, Ugen)
print("\n")

performTTest(Bfit, Ufit, "Fitness")
performTTest(Bgen, Ugen, "Generation")
print("\n")
performWilcoxon(Bfit, Ufit, "Fitness")
performWilcoxon(Bgen, Ugen, "Generation")
#print("\n")
#print(Bfit)
#print(Ufit)
#print(Bgen)
#print(Ugen)

print(len(Bfit))
print(len(Ufit))
