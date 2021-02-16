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


def performTTest(arr1, arr2, name):
    print(name, " ", stats.ttest_ind(arr2, arr1))


problem = 'L2-50-100.txt'
Bfit, Bgen = BRKGA.runWithStatistics(20, 3, problem)
Ufit, Ugen = RKGA.runWithStatistics(20, 3, problem)

print("BRKGA")
performStat(Bfit, Bgen)
print("\n")
print("RKGA")
performStat(Ufit, Ugen)
print("\n")

performTTest(Bfit, Ufit, "Fitness")
performTTest(Bgen, Ugen, "Generation")
