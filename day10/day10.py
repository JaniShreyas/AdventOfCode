with open('data.txt') as f:
    input = [list(line.strip()) for line in f.readlines()]

sLoc = -1
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == 'S':
            sLoc = (i, j)

def getAllPoints():
    points = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            points.append((input[i][j], i, j))
    return points

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
        if (iPrev, jPrev) == (i-1, j):
            valid = (i+1, j)  
        elif (iPrev, jPrev) == (i+1, j):
            valid = (i-1, j)

    elif curChar == '-':
        if (iPrev, jPrev) == (i, j-1):
            valid = (i, j+1)  
        elif (iPrev, jPrev) == (i, j+1):
            valid = (i, j-1)
    
    elif curChar == 'L':
        if (iPrev, jPrev) == (i-1, j):
            valid = (i, j+1) 
        elif (iPrev, jPrev) == (i, j+1):
            valid = (i-1, j)

    
    elif curChar == 'J':
        if (iPrev, jPrev) == (i, j-1):
            valid = (i-1, j)
        elif (iPrev, jPrev) == (i-1, j):
            valid = (i, j-1) 
    
    elif curChar == '7':
        if (iPrev, jPrev) == (i, j-1):
            valid = (i+1, j) 
        elif (iPrev, jPrev) == (i+1, j):
            valid = (i, j-1)
    
    elif curChar == 'F':
        if (iPrev, jPrev) == (i+1, j):
            valid = (i, j+1) 
        elif (iPrev, jPrev) == (i, j+1):
            valid = (i+1, j)

    
    # if valid == None:
    #     raise Exception("Something wrong with Valid Index Calculation")
    
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
        if nextIndex == None:
            continue
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
    print(path[1], path[0], path[-2])
    print(len(path)//2)

def countAtRow(row, loop, pipeAt):
    tp, bp, c = 0, 0, 0
    for j in range(len(input[0])):
        if (row, j) in loop and pipeAt[(row, j)] in '|LJ':
            tp += 1
        if (row, j) in loop and pipeAt[(row, j)] in '|7F':
            bp += 1
        if (row, j) not in loop and tp % 2 and bp % 2:
            c += 1
    return c

def part2():
    path = getPathWithLoop()
    path = path[:-1]
    prevToS = path[-1]
    nextToS = path[1]


    #Hardcoding S's pipe point
    #In this case, its a '|'
    

    path[0] = ('|', path[0][1], path[0][2])
    
    n = len(path)
    loop = []
    pipeAtInd = {}
    
    for node in path:
        char, i, j = node
        loop.append((i, j))
        pipeAtInd[(i, j)] = char
    
    total = sum([countAtRow(row, loop, pipeAtInd) for row in range(len(input))])
    print(total)    

part1()
part2()