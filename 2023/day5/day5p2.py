with open('data.txt') as f:
    input = [line.strip() for line in f.readlines()]

seeds = input[0].split(' ')
seeds = [int(seeds[i]) for i in range(1, len(seeds))]
seedRanges = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds)-1, 2)]

newLineInd = [i for i in range(len(input)) if input[i] == '']

mapList = []
for i in range(len(newLineInd)-1):
    mapList.append(input[newLineInd[i]+1:newLineInd[i+1]])
mapList.append(input[newLineInd[-1]+1:])

mapList = [m[1:] for m in mapList]

mapList = [[[int(num) for num in individual.split(' ')]for individual in m] for m in mapList]

mapDictList = [{(m[i][1], m[i][1] + m[i][2]):m[i][0]-m[i][1]  for i in range(len(m))} for m in mapList]
mapDictList = [dict(sorted(m.items())) for m in mapDictList]

def rangeState(seedR, mapR):
    if (min(seedR[1], mapR[1]) <= max(seedR[0], mapR[0])):
        return 0
    elif ((seedR[1] > mapR[1]) and (seedR[0] < mapR[0])):
        return 1
    elif ((seedR[1] <= mapR[1]) and (seedR[0] >= mapR[0])):
        return 2
    elif ((seedR[0] < mapR[0]) and (seedR[1] > mapR[0]) and (seedR[1] <= mapR[1])):
        return 3
    elif ((seedR[0] >= mapR[0]) and (seedR[0] < mapR[1]) and (mapR[1] < seedR[1])):
        return 4
    raise Exception("something wrong with calculation of range states")

from time import monotonic_ns

start = monotonic_ns()

for i in range(len(mapDictList)):
    mapped = []
    for seedRange in seedRanges:
        remaining = [seedRange]
        while len(remaining) != 0:
            seed = remaining.pop(0)

            isMapped = False
            for ran in mapDictList[i]:
                addValue = mapDictList[i][ran]

                # calculate state
                state = rangeState(seed, ran)
                if state != 0:
                    isMapped = True

                if state == 0:
                    continue

                elif state == 1:
                    remaining.append((seed[0], ran[0]))
                    remaining.append((ran[1], seed[1]))
                    
                    mapped.append((ran[0] + addValue, ran[1] + addValue))
                    break

                elif state == 2:
                    mapped.append((seed[0] + addValue, seed[1] + addValue))
                    break
                
                elif state == 3:
                    remaining.append((seed[0], ran[0]))

                    mapped.append((ran[0] + addValue, seed[1] + addValue))
                    break
                
                elif state == 4:
                    mapped.append((seed[0] + addValue, ran[1] + addValue))

                    remaining.append((ran[1], seed[1]))
                    break
            
            if not isMapped:
                mapped.append(seed)

    seedRanges = list(mapped)

print(min(mapped)[0])
print(monotonic_ns() - start)