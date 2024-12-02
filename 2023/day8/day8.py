import math

with open("data.txt") as f:
    input = [line.strip() for line in f.readlines()]

actions = input[0]
nodes = input[2:]

nodeDict = {}
for node in nodes:
    start, leftRight = node.split(" = ")
    nodeDict[start] = leftRight


# put n = the length of actions
n = len(actions)

def part1():
    # do a while loop for until currentNode != 'ZZZ'
    # start from i = 0 and in the end add 1 to it and then set it to i %= n
    # then decide on the rest of the logic

    #leftIndex = [1:4]
    #rightIndex = [6:9]

    currentNode = 'AAA'
    i = 0
    count = 0
    while currentNode != 'ZZZ':
        currentAction = actions[i]
        options = nodeDict[currentNode]
        if currentAction == 'L':
            currentNode = options[1:4]
        else:
            currentNode = options[6:9]
        i += 1
        i %= n
        count += 1

    print(count)

def part2():

    keys = list(nodeDict.keys())
    currentNodes = [key for key in keys if key[-1] == 'A']
    
    countList = []
    for node in currentNodes:
        i = 0
        count = 0
        currentNode = node
        while currentNode[-1] != 'Z':
            currentAction = actions[i]
            options = nodeDict[currentNode]
            if currentAction == 'L':
                currentNode = options[1:4]
            else:
                currentNode = options[6:9]
            i += 1
            i %= n
            count += 1
        countList.append(count)
    
    lcm = math.lcm(*countList)
    print(lcm)
    
part2()