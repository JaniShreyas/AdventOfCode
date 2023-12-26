from typing import List
from time import monotonic_ns

with open("data.txt") as f:
    data = [line.strip() for line in f.readlines()]

energised: dict[tuple, List[tuple]] = {}

i, j = 0, 0
paths: List[List[tuple[int, int]]] = [[(0, 0), (0, 1)]]


def getNextCoord(cur, dir):
    return (cur[0] + dir[0], cur[1] + dir[1])

def isValidCoord(coord):
    return (coord[0] not in (-1, len(data)) and coord[1] not in (-1, len(data[0])))

# def matchElement(prev, cur, dir):


def part1():
    cur = (0, 0)
    dir = (0, 1)
    energised: dict[tuple, List[tuple]] = {cur: [dir]}
    paths: List[tuple[tuple, tuple]] = [(cur, dir)]

    n = 0
    while len(paths) > 0:
        path = paths[n]
        cur, dir = path[0], path[1]
        prev = (cur[0] - dir[0], cur[1] - dir[1])

        nextCoord = None
        altDir = None
        altNextCoord = None

        element = data[cur[0]][cur[1]]
        match (element):
            case ".":
                # Keep moving
                nextCoord = getNextCoord(cur, dir)
            case "|":
                # check if on same i
                if cur[0] == prev[0]:
                    # Bottom
                    if cur[0] != len(data) - 1:
                        dir = (1, 0)

                    # Top
                    if cur[0] != 0:
                        altDir = (-1, 0)
                        altNextCoord = getNextCoord(cur, altDir)

            case "-":
                # Check if on same j
                if cur[1] == prev[1]:
                    # Right
                    if cur[1] != len(data[0]) - 1:
                        dir = (0, 1)

                    # Left
                    if cur[1] != 0:
                        altDir = (0, -1)
                        altNextCoord = getNextCoord(cur, altDir)

            case "/":
                # Check if on same i
                if cur[0] == prev[0]:
                    # check if from left
                    if prev[1] < cur[1]:
                        dir = (-1, 0)
                    else:
                        dir = (1, 0)
                else:
                    # check if from up
                    if prev[0] < cur[0]:
                        dir = (0, -1)
                    else:
                        dir = (0, 1)
            
            case '\\':
                # Check if on same i
                if cur[0] == prev[0]:
                    # check if from left
                    if prev[1] < cur[1]:
                        dir = (1,0)
                    else:
                        dir = (-1,0)
                else:
                    # check if from up
                    if prev[0] < cur[0]:
                        dir = (0,1)
                    else:
                        dir = (0,-1)
            
        nextCoord = getNextCoord(cur, dir)

        if nextCoord:
            if isValidCoord(nextCoord):
                paths[n] = (nextCoord, dir)
                if nextCoord in energised:
                    if dir in energised[nextCoord]:
                        paths.pop(n)
                    else:
                        energised[nextCoord].append(dir)
                else:
                    energised[nextCoord] = [dir]
            else:
                paths.pop(n)
        
        if altNextCoord and altDir and isValidCoord(altNextCoord):
            paths.append((altNextCoord, altDir))
            if altNextCoord in energised:
                if altDir in energised[altNextCoord]:
                    # paths.pop(n)
                    # I guess this caused a problem because the same thing was just added in nextCoord part
                    # and it either immediately removed it or stopped it before it actually completed
                    # and so I am not sure whether this is good only for my data or for any data in general
                    pass
                else:
                    energised[altNextCoord].append(altDir)
            else:
                energised[altNextCoord] = [altDir]

        if len(paths) == 0:
            break
        
        n += 1
        n %= len(paths)
    print(len(energised))

start = monotonic_ns()
part1()
print("time", monotonic_ns() - start)

def part2():
    pass