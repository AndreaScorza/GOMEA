import numpy as np

def getFitness(el, bidsValue, goodsNumber, bids):
    element = el.copy()
    for x in range(0, len(element)):
        saving = [x, element[x]]
        element[x] = saving
    element.sort(reverse=True, key=lambda x: x[1])

    markedGoods = np.zeros(goodsNumber)
    fitness = 0
    for x in element:
        flag = False
        for y in bids[x[0]]:
            if markedGoods[y] == 1:
                flag = True
        if not flag:
            fitness += bidsValue[x[0]]
            for y in bids[x[0]]:
                markedGoods[y] = 1
    return fitness


