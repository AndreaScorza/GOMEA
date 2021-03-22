
import statistics as stat
from scipy import stats
import ast


def performStat(fit, gen, improv, counter, time):
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
#-----------
    print("\nImprovement: ")
    print("Average: ", stat.mean(improv))
    print("Median:  ", stat.median(improv))
    try:
        print("Mode:    ", stat.mode(improv))
    except:
        print(("Mode:     All values are different"))
    try:
        print("Variance:", stat.variance(improv))
    except:
        print(("Variance: Requires at least two data points"))
    print("St Dev:  ", stat.stdev(improv))
#-----------
    print("\nTotal Gen: ")
    print("Average: ", stat.mean(counter))
    print("Median:  ", stat.median(counter))
    try:
        print("Mode:    ", stat.mode(counter))
    except:
        print(("Mode:     All values are different"))
    try:
        print("Variance:", stat.variance(counter))
    except:
        print(("Variance: Requires at least two data points"))
    print("St Dev:  ", stat.stdev(counter))
#-----------
    print("\nTime: ")
    print("Average: ", stat.mean(time))
    print("Median:  ", stat.median(time))
    try:
        print("Mode:    ", stat.mode(time))
    except:
        print(("Mode:     All values are different"))
    try:
        print("Variance:", stat.variance(time))
    except:
        print(("Variance: Requires at least two data points"))
    print("St Dev:  ", stat.stdev(time))


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
    improvement = []
    counter = []
    time = []
    lines = filter(None, (line.rstrip() for line in open(name)))
    for line in lines:
        fit.append(ast.literal_eval(line)[0])
        gen.append(ast.literal_eval(line)[1])
        improvement.append(ast.literal_eval(line)[2])
        counter.append(ast.literal_eval(line)[3])
        time.append(ast.literal_eval(line)[4])


    return fit, gen, improvement, counter, time

'''problem = 'L3-20-20.txt'
Bfit, Bgen = BRKGA.runWithStatistics(10, 10, problem)
Ufit, Ugen = RKGA.runWithStatistics(10, 10, problem)'''


#Bfit, Bgen, Bimprov, Bcounter, Btime = readFromDataset('Datasets/10L1-250-1000normal.txt')
#Ufit, Ugen, Uimprov, Ucounter, Utime = readFromDataset('Datasets/10L1-250-1000univariate.txt')
Bfit, Bgen, Bimprov, Bcounter, Btime = readFromDataset("Datasets/30L6normal.txt")
Ufit, Ugen, Uimprov, Ucounter, Utime = readFromDataset("Datasets/30L6normal_random.txt")
#Ufit, Ugen, Uimprov, Ucounter, Utime = readFromDataset("Datasets/30L6univariate.txt")

print("\n")
print("GOMEA best individual: ",max(Bfit))
print("RANDOM best individual: ",max(Ufit))
# To make the datasets the same length
if len(Bfit) != len(Ufit):
    while (len(Bfit) < len(Ufit)):
        Ufit.pop()
        Ugen.pop()
        Uimprov.pop() 
        Ucounter.pop()
        Utime.pop()
    while (len(Bfit) > len(Ufit)):
        Bfit.pop()
        Bgen.pop()
        Bimprov.pop()
        Bcounter.pop()
        Btime.pop()

'''
Bfit = Bfit[:100]
Bgen = Bgen[:100]
Bimprov = Bimprov[:100]
Bcounter = Bcounter[:100]
Btime = Btime[:100]
Ufit = Ufit[:100]
Ugen = Ugen[:100]
Uimprov = Uimprov[:100]
Ucounter = Ucounter[:100]
Utime = Utime[:100]'''

print("\n")
print("GOMEA")
performStat(Bfit, Bgen, Bimprov, Bcounter, Btime)
print("\n")
print("RANDOM")
performStat(Ufit, Ugen, Uimprov, Ucounter, Utime)
print("\n")

performTTest(Bfit, Ufit, "Fitness")
performTTest(Bgen, Ugen, "Generation")
performTTest(Bimprov, Uimprov, "Improvement")
performTTest(Bcounter, Ucounter, "Tot Gen")
performTTest(Btime, Utime, "Time")
print("\n")
performWilcoxon(Bfit, Ufit, "Fitness")
performWilcoxon(Bgen, Ugen, "Generation")
performWilcoxon(Bimprov, Uimprov, "Improvement")
performWilcoxon(Bcounter, Ucounter, "Tot Gen")
performWilcoxon(Btime, Utime, "Time")
#print("\n")
#print(Bfit)
#print(Ufit)
#print(Bgen)
#print(Ugen)


