with open('data.txt') as f:
    input = [list(line.strip()) for line in f.readlines()]

sLoc = -1
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == 'S':
            sLoc = (i, j)

def getInitialIndices():
    i, j = sLoc
    n = len(input)
    m = len(input[0])
    validStarts = []
    if i == 0 and j == 0:
        validStarts = [(i+1, j), (i, j+1)]
    elif i == n and j == m:
        validStarts = [(i-1, j), (i, j-1)]
    elif i == 0:
        validStarts = [(i, j-1), (i, j+1), (i+1, j)]
    elif j == 0:
        validStarts = [(i-1, j), (i+1, j), (i, j+1)]
    elif i == n:
        validStarts = [(i, j-1), (i, j+1), (i-1, j)]
    elif j == m:
        validStarts = [(i-1, j), (i+1, j), (i, j-1)]
    else:
        validStarts = [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]
    
    if len(validStarts) == 0:
        raise Exception("Something wrong with getInitialIndices()")

    return validStarts

def getValidIndices(current, last):
    curChar, i, j = current
    lastChar, iPrev, jPrev = last

    valid = None

    if curChar == '.':
        return None
    elif curChar == '|':
        valid = (i+1, j) if (iPrev, jPrev) == (i-1, j) else (i-1, j)

    elif curChar == '-':
        valid = (i, j+1) if (iPrev, jPrev) == (i, j-1) else (i, j-1)
    
    elif curChar == 'L':
        valid = (i, j+1) if (iPrev, jPrev) == (i-1, j) else (i-1, j)
    
    elif curChar == 'J':
        valid = (i-1, j) if (iPrev, jPrev) == (i, j-1) else (i, j-1)
    
    elif curChar == '7':
        valid = (i+1, j) if (iPrev, jPrev) == (i, j-1) else (i, j-1)
    
    elif curChar == 'F':
        valid = (i, j+1) if (iPrev, jPrev) == (i+1, j) else (i+1, j)
    
    if valid == None:
        raise Exception("Something wrong with Valid Index Calculation")
    
    return valid

def getPathWithLoop():
    paths = [[], [], [], []]
    nextIndices = [None, None, None, None]
    paths = [[('S', *sLoc)] for path in paths]
    initialOptions = getInitialIndices()

    for ind in range(len(initialOptions)):
        val = initialOptions[ind]
        inI, inJ = val
        char = input[inI][inJ]
        if inI == sLoc[0] and char == '|':
            continue
        if inJ == sLoc[1] and char == '-':
            continue
        paths[ind].append((char, inI, inJ))
        nextIndex = getValidIndices(paths[ind][-1], paths[ind][-2])
        nextIndices[ind] = nextIndex
    
    # print(paths)
    # print(nextIndices)

    while True:
        isLoopFound = False
        for ind in range(len(paths)):
            nextIndex = nextIndices[ind]
            if nextIndex == None:
                continue
            row, col = nextIndex
            char = input[row][col]
            paths[ind].append((char, row, col))
            if char == 'S':
                isLoopFound = True
                break
            nextIndices[ind] = getValidIndices(paths[ind][-1], paths[ind][-2])
        if isLoopFound:
            break
    
    return paths[ind]
                  

def part1():
    path = getPathWithLoop()
    print(len(path)//2)

part1()