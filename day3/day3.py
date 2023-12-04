# Now, what do we need to do
# Find a way to hash all numbers and their respective indices
# Search for symbols
# Do a search in the 8 indices around it
# Check each index with the hash
# if match exists, add that number to the sum and remove from hash or add to a visited list

# alright, now how to hash
# We can try a dictionary within a dictionary
# with row number as first key, with value dictionary having a (tuple) key with the number as value?
# now suppose number is 3457 at indices 1,2,3,4 respectively, now lets assume star finds index 2 first, it will be a problem
# so let's store all indices in the tuple? no
# let's store the starting and ending values
# on a symbol hit, we will go through all the sub dictionary keys (start, end) and run range(start, end)
# on it and check whether the target index exists within the keys
# if yes, search that start and end index as key, and add the number into the sum
# should work
# but let's see

import re


def surroundingElements(i, j, n):
    # i is row num, j is column num
    if i == 0:
        l = [(i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
    elif i == n:
        l = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1)]
    else:
        l = [
            (i - 1, j - 1),
            (i - 1, j),
            (i - 1, j + 1),
            (i, j - 1),
            (i, j + 1),
            (i + 1, j - 1),
            (i + 1, j),
            (i + 1, j + 1),
        ]

    return l

def part1():

    sum = 0

    with open("data.txt") as f:
        lines = f.readlines()

        nums = {}
        visited = []
        for i in range(len(lines)):
            line = lines[i].strip()

            inner = {}
            m = re.finditer(r"(\d+)", line)
            for match in m:
                s = int(match.start())
                e = int(match.end())
                num = line[s:e]
                inner[(s, e)] = int(num)

            if inner != {}:
                nums[i] = inner

        for i in range(len(lines)):
            line = lines[i].strip()
            for j in range(len(line)):
                char = line[j]
                if not(char.isnumeric() or char == '.'):
                    surrounding = surroundingElements(i,j,len(lines)-1)
                    for surrInd in surrounding:
                        row, col = surrInd
                        if row in nums:
                            for ind in nums[row]:
                                s,e = ind
                                if col in range(s,e):
                                    if (row, ind) not in visited:
                                        number = nums[row][ind]
                                        sum += number
                                        visited.append((row, ind))

    print(sum)

def part2():

    sum = 0

    #need to find *s with exactly 2 adjacent numbers
    with open("data.txt") as f:
        lines = f.readlines()

        nums = {}
        visited = []
        for i in range(len(lines)):
            line = lines[i].strip()

            inner = {}
            m = re.finditer(r"(\d+)", line)
            for match in m:
                s = int(match.start())
                e = int(match.end())
                num = line[s:e]
                inner[(s, e)] = int(num)

            if inner != {}:
                nums[i] = inner
        
        for i in range(len(lines)):
            line = lines[i].strip()
            for j in range(len(line)):
                char = line[j]
                if char == '*':
                    surrounding = surroundingElements(i,j,len(lines)-1)
                    count = 0
                    prod = 1
                    for surrInd in surrounding:
                        row, col = surrInd
                        if row in nums:
                            for ind in nums[row]:
                                s,e = ind
                                if col in range(s,e):
                                    if (row, ind) not in visited:
                                        number = nums[row][ind]
                                        #need to keep a counter and product
                                        #where tho?
                                        count += 1
                                        prod *= number
                                        visited.append((row, ind))
                    if count == 2:
                        sum += prod
    print(sum)

part2()