import BRKGAfinalChromo as BRKGA
import UnbiasedRKGAChromo as RKGA
import GOMEANormal as normal
import GOMEAUnivariate as univariate

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

def creatingDataSetGOMEA(popSize, problem, type):
    if type == "normal":
        population, bestFit, totTime, val, foundAtGen, totFitEval, totNumbOfGen, improvement = normal.GOMEA(popSize, problem)
    elif type == "univariate":
        population, bestFit, totTime, val, foundAtGen, totFitEval, totNumbOfGen, improvement = univariate.GOMEA(popSize, problem)
    fileName = str(popSize)+str(problem).replace(".txt", "")+type+".txt"
    fileName = "/content/drive/MyDrive/" + fileName
    #fileName = "sample.txt"
    file_object = open(fileName, 'a')
    x = [bestFit, foundAtGen, improvement, totNumbOfGen, round(totTime, 3)]
    file_object.write(str(x) + "\n")
    file_object.close()

counter = 0
while counter < 1000:
    print(counter)
    #creatingDataSetBRKGA(10, "L6.txt", "unbiased")
    creatingDataSetGOMEA(30, "L6.txt", "univariate")
    counter += 1