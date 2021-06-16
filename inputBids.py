
def deleteDummy(goodsNumber, bids):
    for a in range(0, len(bids)):
        bids[a] = [x for x in bids[a] if x < goodsNumber]
    return bids

def getAuction(path):
    file = open(path, 'r')
    text2 = file.readlines()
    text = []
    for x in text2:
        if (x[0] != '\n' and x[0] != '%'):
            text.append(x)

    goodsNumber = 0
    bidsNumber = 0
    dummyNumber = 0
    bidsValue = []
    bids = []
    for x in text: # for eachline in text
        if 'good' in x:
            goodsNumber = int(x[5:])
        else:
            if 'bids' in x:
                bidsNumber = int(x[4:])
            else:
                if 'dummy' in x:
                    dummyNumber = int(x[5:])
                else:
                    new = x.split()
                    index = 0
                    value = 0
                    listBid = []
                    for x in range(0, len(new)):
                        if x == 0:
                            index = new[x]
                        else:
                            if x == 1:
                                value = new[x]
                            else:
                                if new[x] != '#':
                                    listBid.append(int(new[x]))
                    bidsValue.append(float(value))
                    bids.append(listBid)

    bids = deleteDummy(goodsNumber, bids)
    returnValue = [goodsNumber, bidsNumber, dummyNumber, bidsValue, bids]
    return (returnValue)


