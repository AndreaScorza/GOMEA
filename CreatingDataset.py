import BRKGAfinalChromo as BRKGA
import UnbiasedRKGAChromo as RKGA

def creatingDataSet(popSize, problem, type):
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

counter = 0
while counter < 1000:
    print(counter)
    creatingDataSet(1000, "L6.txt", "unbiased")
    counter += 1