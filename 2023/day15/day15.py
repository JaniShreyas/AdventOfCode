from typing import List

with open("data.txt") as f:
    data = [line.strip().split(',') for line in f.readlines()][0]

def hash(s):
    #add ascii, mul 17, mod 256
    tot = 0
    for char in s:
        tot += ord(char)
        tot *= 17
        tot %= 256
    
    return tot

def part1():
    tot = 0
    for s in data:
        tot += hash(s)
    print(tot)

# part1()

def part2():
    boxes:List[List[str]] = [[] for i in range(256)]
    for label in data:
        actualLabel = ''
        if label[-1].isnumeric():
            num = 0
            actualLabel = label[:-2]
            h = hash(actualLabel)
            box = boxes[h]
            # I only want to append if it doesn't already exist
            
            for i in range(len(box)):
                l = box[i]
                if l.startswith(actualLabel):
                    boxes[h][i] = actualLabel+label[-1]
                    flag = True
                    break
            else:
                boxes[h].append(actualLabel+str(label[-1]))

                
            if len(box) == 0:
                boxes[h].append(actualLabel+str(label[-1]))
        else:
            actualLabel = label[:-1]
            h = hash(actualLabel)
            box = boxes[h]
            for l in box:
                if l.startswith(actualLabel):
                    boxes[h].remove(l)
    
    s = 0
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            s += (1+i)*(j+1)*(int(boxes[i][j][-1]))
    
    print(s)

part2()