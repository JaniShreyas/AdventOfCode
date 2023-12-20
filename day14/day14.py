import numpy as np

with open("data.txt") as f:
    data = [list(line.strip()) for line in f.readlines()]

arr = np.array(data)

def part1():
    sumList = [0 for i in range(len(arr))]

    for i in range(len(arr[0])):
        col = arr[:, i]
        cubeInd = 1000
        for j in range(len(col)):
            if col[j] == '#':
                cubeInd = j
            elif col[j] == 'O':
                if cubeInd != 1000:
                    sumList[cubeInd+1] += 1
                    cubeInd += 1
                else:
                    sumList[0] += 1
                    cubeInd = 0

    s = 0
    for i in range(len(sumList)):
        factor = len(sumList)-i
        s += factor * sumList[i]

    print(s)

cubePos = [(i,j) for j in range(len(arr[0])) for i in range(len(arr)) if arr[i,j] == '#']

def part2():
    start, end = 0,0
    arr = np.array(data)

    initialArr = np.array(arr)

    sumList = [0 for i in range(len(arr))]
    
    cycleDict = {}

    listOfPositions = []
    initialCirclePos = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i,j] == 'O':
                initialCirclePos.append((i,j))
    initialCirclePos = sorted(initialCirclePos)
    print(initialCirclePos)

    listOfPositions.append(initialCirclePos)

    listOfArrays = [np.array(arr)]

    for ind in range(500):
        # print(ind)
        newPos = []

        # North tilt
        for i in range(len(arr[0])):
            col = arr[:, i]
            cubeInd = 1000
            for j in range(len(col)):
                if col[j] == '#':
                    cubeInd = j
                elif col[j] == 'O':
                    if cubeInd != 1000:
                        newPos.append((cubeInd+1, i))
                        cubeInd += 1
                    else:
                        newPos.append((0, i))
                        cubeInd = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if (i,j) in cubePos:
                    arr[i,j] = '#'
                elif (i,j) in newPos:
                    arr[i,j] = 'O'
                else:
                    arr[i,j] = '.'
        
        newPos = []

        # West tilt
        for i in range(len(arr)):
            row = arr[i, :]
            cubeInd = 1000
            for j in range(len(row)):
                if row[j] == '#':
                    cubeInd = j
                elif row[j] == 'O':
                    if cubeInd != 1000:
                        sumList[cubeInd+1] += 1
                        newPos.append((i, cubeInd+1))
                        cubeInd += 1
                    else:
                        sumList[0] += 1
                        newPos.append((i, 0))
                        cubeInd = 0
                    
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if (i,j) in cubePos:
                    arr[i,j] = '#'
                elif (i,j) in newPos:
                    arr[i,j] = 'O'
                else:
                    arr[i,j] = '.'

        newPos = []

        # South tilt
        for i in range(len(arr[0])):
            col = arr[:, i]
            cubeInd = -1000
            for j in range(len(col)-1, -1, -1):
                if col[j] == '#':
                    cubeInd = j
                elif col[j] == 'O':
                    if cubeInd != -1000:
                        sumList[cubeInd-1] += 1
                        newPos.append((cubeInd-1, i))
                        cubeInd -= 1
                    else:
                        sumList[0] += 1
                        newPos.append((len(col)-1, i))
                        cubeInd = len(col)-1

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if (i,j) in cubePos:
                    arr[i,j] = '#'
                elif (i,j) in newPos:
                    arr[i,j] = 'O'
                else:
                    arr[i,j] = '.'

        # print(newArr)

        # East tilt
        newPos = []

        for i in range(len(arr)):
            row = arr[i, :]
            cubeInd = -1000
            for j in range(len(row)-1, -1, -1):
                if row[j] == '#':
                    cubeInd = j
                elif row[j] == 'O':
                    if cubeInd != -1000:
                        sumList[cubeInd-1] += 1
                        newPos.append((i, cubeInd-1))
                        cubeInd -= 1
                    else:
                        sumList[0] += 1
                        newPos.append((i, len(row) - 1))
                        cubeInd = len(row)-1
                    
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if (i,j) in cubePos:
                    arr[i,j] = '#'
                elif (i,j) in newPos:
                    arr[i,j] = 'O'
                else:
                    arr[i,j] = '.'
        
        s = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i,j] == 'O':
                    s += len(arr)-i
        
        cycleDict[ind] = s
        
        # print(ind, s)

        if ind == 4:
            print(arr)

        flag = False
        for i in range(len(listOfArrays)):
            array = listOfArrays[i]
            if np.array_equal(array, arr):
                print("Found match at:", i)
                start = i
                print("Found match for:", ind)
                end = ind
                flag =True
                break
        if flag:
            break
        listOfArrays.append(np.array(arr))
    print(start, end)
    cycleWhichMatches1b = start + ((1000000000 - start)%(end+1 - start))-1
    print(cycleDict[cycleWhichMatches1b])

def betterPart2():
    arr = np.array(data)

    sums = []
    listOfArrays = [np.array(arr)]
    start, end = 0,0
    for ind in range(500):
        # North tilt
        for j in range(len(arr[0])):
            col = arr[:, j]
            for i in range(len(col)-1, -1, -1):
                for k in range(len(col) - i, 0, -1):
                    if k == len(arr):
                        break
                    if arr[k,j] == 'O':
                        if arr[k-1, j] == '.':
                            arr[k,j], arr[k-1, j] = arr[k-1,j], arr[k,j]
        # West tilt
                            
        for i in range(len(arr)):
            row = arr[i, :]
            for j in range(len(row)-1, -1, -1):
                for k in range(len(row) - j, 0, -1):
                    if k == len(arr):
                        break
                    if arr[i, k] == 'O':
                        if arr[i, k-1] == '.':
                            arr[i,k], arr[i, k-1] = arr[i, k-1], arr[i,k]

        # South tilt
        for j in range(len(arr[0])):
            col = arr[:, j]
            for i in range(len(col)):
                for k in range(len(col) - i -1):
                    if k == len(arr):
                        break
                    if arr[k,j] == 'O':
                        if arr[k+1, j] == '.':
                            arr[k,j], arr[k+1, j] = arr[k+1,j], arr[k,j]

        # East tilt
        for i in range(len(arr)):
            row = arr[i, :]
            for j in range(len(row)):
                for k in range(len(row) - j - 1):
                    if k == len(arr):
                        break
                    if arr[i, k] == 'O':
                        if arr[i, k+1] == '.':
                            arr[i,k], arr[i, k+1] = arr[i, k+1], arr[i,k]
        
        s = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i,j] == 'O':
                    s += len(arr)-i
        
        sums.append(s)

        flag = False
        for i in range(len(listOfArrays)):
            array = listOfArrays[i]
            if np.array_equal(array, arr):
                print("Found match at:", i)
                start = i
                print("Found match for:", ind)
                end = ind
                flag =True
                break
        if flag:
            break
        listOfArrays.append(np.array(arr))
    
    cycleWhichMatches1b = start + ((1000000000 - start)%(end+1 - start))-1
    print(sums[cycleWhichMatches1b])

from time import monotonic
start = monotonic()
betterPart2()
print(f"Time elapsed: {monotonic() - start}")