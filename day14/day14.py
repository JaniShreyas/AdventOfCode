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

def part2():
    sumList = [0 for i in range(len(arr))]
    print(sumList)
    

part2()