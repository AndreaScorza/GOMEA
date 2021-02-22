import BRKGAfinalChromo as BRKGA
import UnbiasedRKGAChromo as RKGA
import statistics as stat
from scipy import stats


def performStat(fit, gen):
    print("\nFitness: ")
    print("Average: ", stat.mean(fit))
    print("Median:  ", stat.median(fit))
    try:
        print("Mode:    ", stat.mode(fit))
    except:
        print(("Mode:     All values are different"))
    try:
        print("Variance:    ", stat.variance(fit))
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
        print("Variance:    ", stat.variance(gen))
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


problem = 'L3-20-20.txt'
Bfit, Bgen = BRKGA.runWithStatistics(10, 10, problem)
print(Bfit)
Ufit, Ugen = RKGA.runWithStatistics(10, 10, problem)

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


