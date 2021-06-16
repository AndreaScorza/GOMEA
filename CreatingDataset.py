#import BRKGAfinalChromo as BRKGA
import UnbiasedRKGAChromo as RKGA
import GOMEANormal as normal
import GOMEAUnivariate as univariate
import GOMEA4testFinal as GOMEA
import BRKGA as BRKGA
import deceptiveGomeaForDeflen6AndLoose as deceptive

def creatingDataSetBRKGA(popSize, problem, type):
    if type == "biased":
        bestFitness, storedPop, lastPopulation, totalTime, foundAtGen, totFitEval = BRKGA.BRKGAchromo(popSize, problem)
    elif type == "unbiased":
        bestFitness, storedPop, lastPopulation, totalTime, foundAtGen = RKGA.BRKGAchromo(popSize, problem)
    fileName = str(popSize)+str(problem).replace(".txt", "")+type+".txt"
    fileName = "/content/drive/MyDrive/" + fileName
    #fileName = "sample.txt"
    file_object = open(fileName, 'a')
    x = [bestFitness, foundAtGen]
    file_object.write(str(x) + "\n")
    file_object.close()

def creatingDataSetGOMEA(popSize, problem, type, randomLt):
    if type == "normal":
        population, bestFit, totTime, val, foundAtGen, totFitEval, totNumbOfGen, improvement = normal.GOMEA(popSize, problem, randomLt)
    elif type == "univariate":
        population, bestFit, totTime, val, foundAtGen, totFitEval, totNumbOfGen, improvement = univariate.GOMEA(popSize, problem)
    if randomLt:
        fileName = str(popSize) + str(problem).replace(".txt", "") + type + "_random.txt"
    else:
        fileName = str(popSize) + str(problem).replace(".txt", "") + type + ".txt"
    fileName = "/content/drive/MyDrive/" + fileName
    #fileName = "sample.txt"
    file_object = open(fileName, 'a')
    x = [bestFit, foundAtGen, improvement, totNumbOfGen, round(totTime, 3)]
    file_object.write(str(x) + "\n")
    file_object.close()


def writeToFile(times, name, popsize, type):
    for x in range(0, times):
        fileName = "/content/drive/MyDrive/" + name
        #fileName = name
        file_object = open(fileName, 'a')
        if type == 'gomea':
            #x = GOMEA.GOMEA(popsize, "L1-L6-L7/L1-25-30.txt")
            x = GOMEA.GOMEA(popsize, "L7.txt")
        elif type == 'brkga':
            x = BRKGA.BRKGAchromo(popsize, "L3-100-300.txt")
        file_object.write(str(x) + "\n")
        file_object.close()

writeToFile(8, 'GOMEA-L7-256-1000-UNIVARIATE.txt', 60, 'gomea')

def writeToFileDeceptive(times, name, popsize, type, order):
    for x in range(0, times):
        fileName = "/content/drive/MyDrive/" + name
        #fileName = name
        file_object = open(fileName, 'a')
        x = deceptive.GOMEA(popsize, type, order)
        file_object.write(str(x) + "\n")
        file_object.close()

#writeToFileDeceptive(10, 'relativeLoose100.txt', 100, 'relative', 'loose')


'''counter = 0
while counter < 1000:
    print(counter)
    #creatingDataSetBRKGA(10, "L6.txt", "unbiased")
    creatingDataSetGOMEA(30, "L6.txt", "normal", False)
    counter += 1'''