with open('data.txt') as f:
    lines = [line.strip() for line in f.readlines()]

    springs = []
    groups = []
    for line in lines:
        lineSplitted = line.strip().split(' ')
        springs.append(list(lineSplitted[0]))
        groups.append(list(map(int, lineSplitted[1].split(','))))

def recursion(spring, group):

    unknownPos = 1000
    for i in range(len(spring)):
        if spring[i] == '?':
            unknownPos = i
            break

    # Finding the first group of #s
    hashStart = 1000
    hashEnd = 1000
    isStartFound = False
    for i in range(len(spring)):
        if not isStartFound and spring[i] == '#':
            hashStart = i
            isStartFound = True
        if isStartFound and spring[i] != '#':
            hashEnd = i
            break
    
    if hashStart != 1000 and hashEnd == 1000:
        hashEnd = len(spring)

    count = hashEnd - hashStart
    if hashStart < unknownPos:
        if count == group[0]:
            spring = spring[hashEnd+1:]
            group = group[1:]
        elif count > group[0]:
            return 0
        else:
            if unknownPos == 1000:
                return 0

    unknownPos = 1000
    for i in range(len(spring)):
        if spring[i] == '?':
            unknownPos = i
            break
    
    if len(group) != 0 and len(spring) == 0:
        return 0

    if len(group) == 0:
        if '#' in spring:
            return 0
        else:
            return 1

    # if len(group) != 0:
    #     if not('.' in spring or '?' in spring):
    #         return 0
            
    if unknownPos == 1000 and '#' not in spring:
        return 0
    
    
    newSpring1 = spring[0:unknownPos] + ['#'] + spring[unknownPos+1:]
    newSpring2 = spring[0:unknownPos] + ['.'] + spring[unknownPos+1:]
    
    a = recursion(newSpring1, group)
    b = recursion(newSpring2, group)

    print(spring, group, a, b)

    return a + b
    
    
i = 0
arra = recursion(springs[i], groups[i])
print(arra)

s = 0
for i in range(len(springs)):
    arrangements = recursion(springs[i], groups[i])
    s += arrangements

print(s)