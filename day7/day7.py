with open("data.txt") as f:
    input = [line.strip() for line in f.readlines()]

strength = [str(num) for num in range(2, 10)]
strength.extend(['T', 'J', 'Q', 'K', 'A'])

hands = [line[:5] for line in input]
bids = [int(line.split(' ')[1]) for line in input]

# print(hands)

# Greater index means greater strength

# We need to rank the hands given their types
# types are: five of a kind, four of a kind, full house, three of a kind, two pair, one pair, high card

# for every hand, we will create a count dict of each card
# then sort it by value
# then if highest value is 5, it is a 5 of a kind bid, if 4 it is 4 of, if it is 3 and there are only 2 keys it is full house
# if it is 3 and there are total 3 keys, it is 3 of a, if it is 2 and there are total 3 keys, it is 2 pair
# if it is 2 and there are total 4 keys, it is a 1 pair and if there are total 5 keys, it is a high card

# let's encode high as 0, 1pair as 1, 2pair as 2, 3kind as 3, full as 4, 4kind as 5, 5kind as 6
typeDict = {}

for hand in hands:
    countDict = {}
    for card in hand:
        if card in countDict:
            countDict[card] += 1
        else:
            countDict[card] = 1
    
    sortedCountDict = dict(sorted(countDict.items(), key=lambda x:x[1], reverse=True))
    keys = list(sortedCountDict.keys())
    values = list(sortedCountDict.values())

    if values[0] == 5:
        typeDict[hand] = 6
    elif values[0] == 4:
        typeDict[hand] = 5
    elif (values[0] == 3) and (len(keys) == 2):
        typeDict[hand] = 4
    elif (values[0] == 3) and (len(keys) == 3):
        typeDict[hand] = 3
    elif (values[0] == 2) and (len(keys) == 3):
        typeDict[hand] = 2
    elif (values[0] == 2) and (len(keys) == 4):
        typeDict[hand] = 1
    elif len(keys) == 5:
        typeDict[hand] = 0

high = [key for key in typeDict if typeDict[key] == 0]
one = [key for key in typeDict if typeDict[key] == 1]
two = [key for key in typeDict if typeDict[key] == 2]
three = [key for key in typeDict if typeDict[key] == 3]
full = [key for key in typeDict if typeDict[key] == 4]
four = [key for key in typeDict if typeDict[key] == 5]
five = [key for key in typeDict if typeDict[key] == 6]

handTypeList = [high, one, two, three, full, four, five]

#outputs h1 < h2
def lessThan(h1, h2):
    flag = False
    for n in range(len(h1)):
        st1 = strength.index(h1[n])
        st2 = strength.index(h2[n])
        if st1 == st2:
            continue
        elif st1 < st2:
            return True
        elif st1 > st2:
            return False
    
    return flag

for i in range(len(handTypeList)):
    for j in range(len(handTypeList[i])):
        minInd = j
        for k in range(j+1, len(handTypeList[i])):
            if lessThan(handTypeList[i][k], handTypeList[i][minInd]):
                minInd = k
        handTypeList[i][j], handTypeList[i][minInd] = handTypeList[i][minInd], handTypeList[i][j]

handTypeList = [ele for ele in handTypeList if ele != []]

output = 0
rank=1
for i in range(len(handTypeList)):
    for j in range(len(handTypeList[i])):
        h = handTypeList[i][j]
        ind = hands.index(h)
        bid = bids[ind]
        output += bid * rank
        rank+=1

print(output)

strengthPart2 = ['J']
strengthPart2.extend([str(num) for num in range(2, 10)])
strengthPart2.extend(['T', 'Q', 'K', 'A'])

print(strengthPart2)