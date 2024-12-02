import numpy as np

with open("data.txt") as f:
    input = [list(line.strip()) for line in f.readlines()]

def sumOfDist(size = 2):
    arr = np.array(input)

    allEmptyRows = []
    for i in range(len(arr)):
        if list(arr[i, :]) == ['.' for i in range(len(arr[0]))]:
            allEmptyRows.append(i)

    allEmptyCols = []
    for j in range(len(arr[0])):
        if list(arr[:, j]) == ['.' for j in range(len(arr))]:
            allEmptyCols.append(j)
    
    galaxyIndices = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i,j] == '#':
                galaxyIndices.append((i,j))

    dist = 0
    for i in range(len(galaxyIndices)):
        x1,y1 = galaxyIndices[i]
        distList = []
        for j in range(i+1, len(galaxyIndices)):
            x2, y2 = galaxyIndices[j]
            originalDist = abs(x2-x1)+abs(y2-y1)
            numRowsLess = 0
            for emptyRow in allEmptyRows:
                if (x1 < emptyRow and x2 > emptyRow) or (x1 > emptyRow and x2 < emptyRow):
                    numRowsLess += 1
            originalDist += numRowsLess*(size - 1)

            numColsLess = 0
            for emptyCol in allEmptyCols:
                if (y1 < emptyCol and y2 > emptyCol) or (y1 > emptyCol and y2 < emptyCol):
                    numColsLess += 1
            originalDist += numColsLess*(size - 1)
            distList.append(originalDist)
        dist += sum(distList)
    print(dist)

sumOfDist(size=2)
sumOfDist(size=1000000)