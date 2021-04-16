import inputBids as auction
import numpy as np
import decoder as dc
import random
goodsNumber, bidsNumber, dummyNumber, bidsValue, bids = auction.getAuction("problemInstances/L3-20-20.txt")

'''vector = []
for x in range(0, bidsNumber):
    vector.append(x)'''




vector = random.sample(list(range(bidsNumber)), bidsNumber)
#print(vector)
#print(bids,"\n", bidsValue)
#print(dc.getFitnessLocalSearch(vector, bids, bidsValue, goodsNumber))

#vector=[3,1,2,4,0]
# mylist.insert(0, mylist.pop(mylist.index(targetvalue)))
fitness = dc.getFitnessLocalSearch(vector, bids, bidsValue, goodsNumber)

def cycle(vector, fitness):
    for x in range(0, bidsNumber-1):
        print(bidsNumber-(x+1))
        newVec = vector.copy()
        newVec.insert(0, newVec.pop(bidsNumber-(x+1)))
        newFit = dc.getFitnessLocalSearch(newVec, bids, bidsValue, goodsNumber)
        if newFit > fitness:
            return  newVec, newFit, True # 1 mean there was an improvement
    return vector, fitness, False # 0 for no improvement

print(vector, " ", fitness)
vector, fitness, improv = cycle(vector, dc.getFitnessLocalSearch(vector,bids,bidsValue,goodsNumber))

while(improv == True):
    vector, fitness, improv = cycle(vector, dc.getFitnessLocalSearch(vector, bids, bidsValue, goodsNumber))
    print(vector, " ", fitness)

print("End meyhod 1")
vector = random.sample(list(range(bidsNumber)), bidsNumber)
def ciclo(vector, insertPos, fitness):
    x = 0
    while x < bidsNumber - (insertPos+1):
        print(insertPos, " ", bidsNumber-(x+1))
        newVec = vector.copy()
        newVec.insert(insertPos, newVec.pop(bidsNumber - (x + 1)))
        newFit = dc.getFitnessLocalSearch(newVec, bids, bidsValue, goodsNumber)
        x += 1
        if newFit > fitness:
            print(vector, fitness)
            vector = newVec
            fitness = newFit
            x = 0
    return vector, fitness


y = 0
while y < bidsNumber-1:
    vector, fitness = ciclo(vector, y, dc.getFitnessLocalSearch(vector, bids, bidsValue, goodsNumber))
    print(vector, fitness)
    y += 1
    print("\n")
