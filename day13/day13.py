import numpy as np

with open('data.txt') as f:
    data = [line.strip() for line in f.readlines()]

newlineInd = [ind for ind in range(len(data)) if data[ind] == '']

groups = [[] for i in range(len(newlineInd)+1)]
groups[0] = [list(data[i])for i in range(newlineInd[0])]
for i in range(1,len(newlineInd)):
    ind = newlineInd[i]
    groups[i] = [list(data[i]) for i in range(newlineInd[i-1]+1, ind)]

groups[-1] = [list(data[i]) for i in range(newlineInd[-1]+1, len(data))]

def part1():
    vertical = 0
    horizontal = 0
    for pattern in groups:
        arr = np.array(pattern)
        # print(arr.shape)

        # Vertical Reflections
        for i in range(len(arr[0])-1):
            col1 = arr[:, i]
            col2 = arr[:, i+1]
            if np.array_equal(col1, col2):
                # print((i, i+1))
                leftCols = i+1
                rightCols = len(arr[0])-(i+1)
                isNotReflection = False
                for j in range(1, min(leftCols, rightCols)):
                    # print(i-j, i+j+1)
                    if not np.array_equal(arr[:, i-j], arr[:, i+j+1]):
                        isNotReflection = True
                        break
                if not isNotReflection:
                    vertical += leftCols
        
        # print("\n\n\n\n\n")
        # Horizontal Reflections
        for i in range(len(arr)-1):
            row1 = arr[i, :]
            row2 = arr[i+1, :]
            if np.array_equal(row1, row2):
                # print(arr.shape)
                # print((i, i+1))
                upRows = i+1
                downRows = len(arr)-(i+1)
                isNotReflection = False
                for j in range(1, min(upRows, downRows)):
                    # print(i-j, i+j+1)
                    if not np.array_equal(arr[i-j, :], arr[i+j+1, :]):
                        isNotReflection = True
                        break
                if not isNotReflection:
                    horizontal += upRows

    total = vertical + 100*horizontal
    print(total)

def part2():
    # Suppose I am searching for a new vertical column
    # I will search for a pair of adjacents which are equal and again check for any dicrepency
    # When I find one, I will go through all the corresponding pair of cells (in the same row)
    # And I'll keep track of the number of pairs that are different
    # If the no. is greater than 1, break, because this pair would clearly not work
    # if the no. is 1, assume this will work and keep moving
    # keep count of the no. of discrepencies and only if they are > 0, add the no. of left columns to vertical
    # do the same for horizontal reflection

    vertical = 0
    horizontal = 0
    for pattern in groups:
        arr = np.array(pattern)
        for i in range(len(arr[0])-1):
            smudgeCount = 0
            col1 = arr[:, i]
            col2 = arr[:, i+1]
            iniDiffCount = 0
            for k in range(len(col1)):
                if col1[k] != col2[k]:
                    iniDiffCount += 1
            if iniDiffCount <= 1:
                smudgeCount += iniDiffCount
                # print((i, i+1))
                leftCols = i+1
                rightCols = len(arr[0])-(i+1)
                isNotReflection = False
                for j in range(1, min(leftCols, rightCols)):
                    # print(i-j, i+j+1)
                    if not np.array_equal(arr[:, i-j], arr[:, i+j+1]):
                        diffCount = 0
                        for k in range(len(arr[:, i-j])):
                            if arr[:, i-j][k] != arr[:, i+j+1][k]:
                                diffCount += 1
                        if diffCount > 1:
                            isNotReflection = True
                            break
                        else:
                            smudgeCount += 1
                if not isNotReflection and smudgeCount != 0:
                    vertical += leftCols
        
        for i in range(len(arr)-1):
            smudgeCount = 0
            row1 = arr[i, :]
            row2 = arr[i+1, :]
            iniDiffCount = 0
            for k in range(len(row1)):
                if row1[k] != row2[k]:
                    iniDiffCount += 1
            if iniDiffCount <= 1:
                smudgeCount += iniDiffCount
                # print((i, i+1))
                upRows = i+1
                downRows = len(arr)-(i+1)
                isNotReflection = False
                for j in range(1, min(upRows, downRows)):
                    # print(i-j, i+j+1)
                    if not np.array_equal(arr[i-j, :], arr[i+j+1, :]):
                        diffCount = 0
                        for k in range(len(arr[i-j, :])):
                            if arr[i-j, :][k] != arr[i+j+1, :][k]:
                                diffCount += 1
                        if diffCount > 1:
                            isNotReflection = True
                            break
                        else:
                            smudgeCount += 1
                if not isNotReflection and smudgeCount != 0:
                    horizontal += upRows
                    
    total = vertical + 100*horizontal
    print(total)
    
                        
part2()