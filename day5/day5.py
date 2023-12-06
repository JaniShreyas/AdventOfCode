# First let's separate all the different things
# 1. Seeds, 2. seed-to-soil, 3. seed-to-fertilizer, 4. fertilizier-to-water, 5. water-to-light, 6. light-to-temperature,
# 7. temperature-to-humidity, 8. humidity-to-location

with open('data.txt') as f:
    input = [line.strip() for line in f.readlines()]

seed = input[0].split(' ')

newLineInd = [i for i in range(len(input)) if input[i] == '']
# print(newLineInd)

seedToSoil = input[newLineInd[0]+1: newLineInd[1]]
soilToFertilizer = input[newLineInd[1]+1: newLineInd[2]]
fertilizerToWater = input[newLineInd[2]+1: newLineInd[3]]
waterToLight = input[newLineInd[3]+1: newLineInd[4]]
lightToTemperature = input[newLineInd[4]+1: newLineInd[5]]
temperatureToHumidity = input[newLineInd[5]+1: newLineInd[6]]
humidityToLocation = input[newLineInd[6]+1:]

# print(seed[0], seedToSoil[0],soilToFertilizer[0], fertilizerToWater[0], waterToLight[0], lightToTemperature[0], temperatureToHumidity[0], humidityToLocation[0])

seed = [int(s) for s in seed[1:]]

seedToSoil = [(s.split(' ')) for s in seedToSoil[1:]]
soilToFertilizer = [(s.split(' '))for s in soilToFertilizer[1:]]
fertilizerToWater = [(s.split(' ')) for s in fertilizerToWater[1:]]
waterToLight = [(s.split(' ')) for s in waterToLight[1:]]
lightToTemperature = [(s.split(' ')) for s in lightToTemperature[1:]]
temperatureToHumidity = [(s.split(' ')) for s in temperatureToHumidity[1:]]
humidityToLocation = [(s.split(' ')) for s in humidityToLocation[1:]]

seedToSoil = [[int(s) for s in seedToSoil[i]] for i in range(len(seedToSoil))]
soilToFertilizer = [[int(s) for s in soilToFertilizer[i]] for i in range(len(soilToFertilizer))]
fertilizerToWater = [[int(s) for s in fertilizerToWater[i]] for i in range(len(fertilizerToWater))]
waterToLight = [[int(s) for s in waterToLight[i]] for i in range(len(waterToLight))]
lightToTemperature = [[int(s) for s in lightToTemperature[i]] for i in range(len(lightToTemperature))]
temperatureToHumidity = [[int(s) for s in temperatureToHumidity[i]] for i in range(len(temperatureToHumidity))]
humidityToLocation = [[int(s) for s in humidityToLocation[i]] for i in range(len(humidityToLocation))]

# now I have all the data in the form of the list in its most basic form
# I need to turn it

seedToSoilDict = {(seedToSoil[i][1], seedToSoil[i][1] + seedToSoil[i][2]):(seedToSoil[i][0], seedToSoil[i][0] + seedToSoil[i][2]) for i in range(len(seedToSoil))}
soilToFertilizerDict = {(soilToFertilizer[i][1], soilToFertilizer[i][1] + soilToFertilizer[i][2]):(soilToFertilizer[i][0], soilToFertilizer[i][0] + soilToFertilizer[i][2]) for i in range(len(soilToFertilizer))}
fertilizerToWaterDict = {(fertilizerToWater[i][1], fertilizerToWater[i][1] + fertilizerToWater[i][2]):(fertilizerToWater[i][0], fertilizerToWater[i][0] + fertilizerToWater[i][2]) for i in range(len(fertilizerToWater))}
waterToLightDict = {(waterToLight[i][1], waterToLight[i][1] + waterToLight[i][2]):(waterToLight[i][0], waterToLight[i][0] + waterToLight[i][2]) for i in range(len(waterToLight))}
lightToTemperatureDict = {(lightToTemperature[i][1], lightToTemperature[i][1] + lightToTemperature[i][2]):(lightToTemperature[i][0], lightToTemperature[i][0] + lightToTemperature[i][2]) for i in range(len(lightToTemperature))}
temperatureToHumidityDict = {(temperatureToHumidity[i][1], temperatureToHumidity[i][1] + temperatureToHumidity[i][2]):(temperatureToHumidity[i][0], temperatureToHumidity[i][0] + temperatureToHumidity[i][2]) for i in range(len(temperatureToHumidity))}
humidityToLocationDict = {(humidityToLocation[i][1], humidityToLocation[i][1] + humidityToLocation[i][2]):(humidityToLocation[i][0], humidityToLocation[i][0] + humidityToLocation[i][2]) for i in range(len(humidityToLocation))}

seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []

# alright, now I have the maps with the range of source as keys and range of destination as values
# now I beed to search through all the seed numbers, find their map to fertilizer, then that ferilizers map to water, and so on until location
# and save it as {seed: location}
# then find the key with minimum value
#should be easy

newRange = []
for i in range(0, len(seed), 2):
    newRange.append((seed[i], seed[i] + seed[i+1]))

def part1():

    seedS = {}
    soilF = {}
    fW = {}
    wL = {}
    lT = {}
    tH ={}
    hL = {}

    for s in seed:
        # if it is in the range of keys to fertilizer, then use its corresponding value, otherwise use it as it is
        sToSoilKeys = list(seedToSoilDict.keys())
        sToSoilValues = list(seedToSoilDict.values())
        isInRange = False
        for i in range(len(sToSoilKeys)):
            start, end = sToSoilKeys[i]
            startVal, endVal = sToSoilValues[i]

            if s >= start and s < end:
                j = s - start
                seedS[s] = startVal+j
                isInRange = True
            
        if not isInRange:
            seedS[s] = s

    for val in seedS.values():
        # if it is in the range of keys to fertilizer, then use its corresponding value, otherwise use it as it is
        sToFKeys = list(soilToFertilizerDict.keys())
        sToFValues = list(soilToFertilizerDict.values())
        isInRange = False
        for i in range(len(sToFKeys)):
            start, end = sToFKeys[i]
            startVal, endVal = sToFValues[i]

            if val >= start and val < end:
                j = val-start
                soilF[val] = startVal+j
                isInRange = True

        if not isInRange:
            soilF[val] = val

    for val in soilF.values():
        fToWKeys = list(fertilizerToWaterDict.keys())
        fToWValues = list(fertilizerToWaterDict.values())
        
        isInRange = False
        for i in range(len(fToWKeys)):
            start, end = fToWKeys[i]
            startVal, endVal = fToWValues[i]

            if val >= start and val < end:
                j = val-start
                fW[val] = startVal+j
                isInRange = True
            
        if not isInRange:
            fW[val] = val

    for val in fW.values():
        wToLKeys = list(waterToLightDict.keys())
        wToLValues = list(waterToLightDict.values())
        
        isInRange = False
        for i in range(len(wToLKeys)):
            start, end = wToLKeys[i]
            startVal, endVal = wToLValues[i]

            if val >= start and val < end:
                j = val-start
                wL[val] = startVal+j
                isInRange = True
                
        if not isInRange:
            wL[val] = val

    for val in wL.values():
        lToTKeys = list(lightToTemperatureDict.keys())
        lToTValues = list(lightToTemperatureDict.values())
        
        isInRange = False
        for i in range(len(lToTKeys)):
            start, end = lToTKeys[i]
            startVal, endVal = lToTValues[i]

            if val >= start and val < end:
                j = val-start
                lT[val] = startVal+j
                isInRange = True
            
        if not isInRange:
            lT[val] = val

    for val in lT.values():
        tToHKeys = list(temperatureToHumidityDict.keys())
        tToHValues = list(temperatureToHumidityDict.values())
        
        isInRange = False
        for i in range(len(tToHKeys)):
            start, end = tToHKeys[i]
            startVal, endVal = tToHValues[i]

            if val >= start and val < end:
                j = val-start
                tH[val] = startVal+j
                isInRange = True
        if not isInRange:
            tH[val] = val

    for val in tH.values():
        hToLKeys = list(humidityToLocationDict.keys())
        hToLValues = list(humidityToLocationDict.values())
        
        isInRange = False
        for i in range(len(hToLKeys)):
            start, end = hToLKeys[i]
            startVal, endVal = hToLValues[i]

            if val >= start and val < end:
                j = val-start
                hL[val] = startVal+j
                isInRange = True
            
        if not isInRange:
            hL[val] = val

    loc = []
    for s in seed:
        l = hL[tH[lT[wL[fW[soilF[seedS[s]]]]]]]
        loc.append(l)

    print(min(loc))

newSeedToSoil = {}
newSoilToFert = {}
newFertToWater = {}
newWaterToLight = {}
newLightToTemp = {}
newTempToHum = {}
newHumToLoc = {}

oldDicts = [seedToSoilDict, soilToFertilizerDict, fertilizerToWaterDict, waterToLightDict, lightToTemperatureDict, temperatureToHumidityDict, humidityToLocationDict]
newDicts = [newSeedToSoil, newSoilToFert, newFertToWater, newWaterToLight, newLightToTemp, newTempToHum, newHumToLoc]
for i in range(len(newDicts)):
    for key in oldDicts[i]:
        start, end = key
        startVal, endVal = oldDicts[i][key]
        newDicts[i][key] = startVal - start
    newDicts[i] = dict(sorted(newDicts[i].items()))

# print(newRange)
# mapRange = []

# while newRange != []:
#     s = newRange[0]
#     seedStart, seedEnd = s

#     if seedStart >= any(newRange) and seedEnd <= any(newRange):
#         keys = newSeedToSoil.keys()
#         for key in keys:
#             mStart, mEnd = key
#             if seedStart >= mStart and seedEnd <= mEnd:
#                 mapRange.append((seedStart + newSeedToSoil[key], seedEnd + newSeedToSoil[key]))
#                 newRange.remove(s)
#             elif seedStart >= mStart and seedEnd > mEnd:
#                 mapRange.append((seedStart + newSeedToSoil[key], mEnd + newSeedToSoil[key]))
#                 newRange.remove(s)
#                 newRange.append((mEnd, seedEnd))
#     elif seedStart < all(newRange) and seedEnd <= any(newRange):
#         keys = newSeedToSoil.keys()
#         for key in keys:
#             mStart, mEnd = key
#             if seedEnd >= mStart and seedEnd <= mEnd:
#                 mapRange.append((mStart + newSeedToSoil[key], seedEnd + newSeedToSoil[key]))
#                 newRange.remove(s)
#                 mapRange.append((seedStart, mStart))
#     else:
#         # keys = newSeedToSoil.keys()
#         # for key in keys:
#         #     mStart, mEnd = key
#         #     mapRange.append()
#         pass

# print(mapRange)

#Now I need tofind where the seed start is < mStart

#Assumes sorted List
#ind = 0 checks for start, = 1 checks for end
def posWhereLess(seedR, mapRangeList, ind):
    for i in range(len(mapRangeList)):
        mStart, mEnd = mapRangeList[i]
        if seedR[ind] <= mapRangeList[i][ind]:
            return i

ListOfmapRangeList = []
for i in range(len(newDicts)):
    ListOfmapRangeList.append(list(newDicts[i].keys()))

print(posWhereLess(newRange[0], ListOfmapRangeList[0], ind = 1))

# #map is the index in newDicts
# def mappedRanges(seedRange, mapRangeList, rangeInd):
#     mappedList = []

#     for seed in seedRange:
#         print("seed:",seed)
#         posStart = posWhereLess(seed, mapRangeList[rangeInd], ind = 0)
#         posEnd = posWhereLess(seed, mapRangeList[rangeInd], ind = 1)
        
#         if posStart == None:
#             posStart = len(mapRangeList[rangeInd])
#         if posEnd == None:
#             posEnd = len(mapRangeList[rangeInd])

#         if(posStart == len(mapRangeList[rangeInd])):
#             mappedList.append(seed)
#             # return mappedList
#         else:
#             mappedList.append((seed[0] + newDicts[rangeInd][mapRangeList[rangeInd][posStart-1]], mapRangeList[rangeInd][posStart-1][1] + newDicts[rangeInd][mapRangeList[rangeInd][posStart-1]]))

#         for i in range(posStart, posEnd):
#             mappedList.append((mapRangeList[rangeInd][i][0] + newDicts[rangeInd][mapRangeList[rangeInd][i]], mapRangeList[rangeInd][i][1] + newDicts[rangeInd][mapRangeList[rangeInd][i]]))
#             if (i+1 < posEnd) and (mapRangeList[rangeInd][i][1] != mapRangeList[rangeInd][i+1][0]):
#                 mappedList.append((mapRangeList[rangeInd][i][1], mapRangeList[rangeInd][i+1][0]))
        
#         if not (posStart > posEnd) and not(posEnd >= len(mapRangeList[rangeInd])):
#             mapRangeList.append((mapRangeList[rangeInd][posEnd][0] + newDicts[rangeInd][mapRangeList[rangeInd][posEnd]], seed[1] + newDicts[rangeInd][mapRangeList[rangeInd][posEnd]]))
    
#     return mappedList

# print(mappedRanges(newRange, ListOfmapRangeList, rangeInd = 0))

# def part2():
#     seedRange = newRange
#     for i in range(len(ListOfmapRangeList)):
#         mappedRng = mappedRanges(seedRange, ListOfmapRangeList, i)
#         seedRange = list(mappedRng)
#         print(seedRange, i)
    
#     print(seedRange)

# part2()
# # print(mappedRanges(newRange, ListOfmapRangeList, 0))


#map seed to soil
newSeedToSoil = newDicts[0]
seedToSoil = ListOfmapRangeList[0]
print(seedToSoil)

ssmapped = []
for s in newRange:
    print(s)
    posStart = posWhereLess(s, seedToSoil, 0)
    posEnd = posWhereLess(s, seedToSoil, 1)
    
    if posStart == None and posEnd == None:
        ssmapped.append(s)
    elif posStart == None:
        addValue = newSeedToSoil[seedToSoil[posEnd]]
        ssmapped.append((s[0] + addValue, s[1] + addValue))
    
    elif posStart-1 == posEnd:
        addValue = newSeedToSoil[seedToSoil[posStart-1]]
        ssmapped.append((s[0]+addValue, s[1]+addValue))
    elif posStart >= posEnd:
        #ranges are: s[0], seedToSoil[posEnd][1]
        #then a loop from posStart, posEnd
        # in this loop seedToSoil[i][0], seedToSoil[i][1]
        # and also check for any in between values with
        # seedToSoil[i][1] != seedToSoil[i+1][0] as long as i < len(seedToSoil)
        # and if this is the case, range is (seedToSoil[i][1], seedToSoil[i+1][0])
        #then seedToSoil[posEnd][0], s[1]
        addValue = newSeedToSoil[seedToSoil[posStart-1]]
        ssmapped.append((s[0] + addValue, seedToSoil[posEnd-1][1] + addValue))

        for i in range(posStart, posEnd):
            addValue = newSeedToSoil[seedToSoil[i]]
            ssmapped.append((seedToSoil[i][0] + addValue, seedToSoil[i][1]))
            if i+1 < len(seedToSoil):
                if seedToSoil[i][1] != seedToSoil[i+1][0]:
                    ssmapped.append(seedToSoil[i])
        
        addValue = newSeedToSoil[seedToSoil[posEnd]]
        ssmapped.append((seedToSoil[posEnd][0]+addValue, s[1] + addValue))


print(ssmapped)

newSoilToFert = newDicts[1]
soilToFert = ListOfmapRangeList[1]
sfmapped = []
for s in ssmapped:
    print(s)
    posStart = posWhereLess(s, soilToFert, 0)
    posEnd = posWhereLess(s, soilToFert, 1)
    
    if posStart == None and posEnd == None:
        sfmapped.append(s)
    elif posStart == None:
        addValue = newSoilToFert[soilToFert[posEnd]]
        sfmapped.append((s[0] + addValue, s[1] + addValue))
    
    elif posStart-1 == posEnd:
        addValue = newSoilToFert[soilToFert[posStart-1]]
        sfmapped.append((s[0]+addValue, s[1]+addValue))
    elif posStart >= posEnd:
        #ranges are: s[0], soilToFert[posEnd][1]
        #then a loop from posStart, posEnd
        # in this loop soilToFert[i][0], soilToFert[i][1]
        # and also check for any in between values with
        # soilToFert[i][1] != soilToFert[i+1][0] as long as i < len(soilToFert)
        # and if this is the case, range is (soilToFert[i][1], soilToFert[i+1][0])
        #then soilToFert[posEnd][0], s[1]
        addValue = newSoilToFert[soilToFert[posStart-1]]
        sfmapped.append((s[0] + addValue, soilToFert[posEnd-1][1] + addValue))

        for i in range(posStart, posEnd):
            addValue = newSoilToFert[soilToFert[i]]
            sfmapped.append((soilToFert[i][0] + addValue, soilToFert[i][1]))
            if i+1 < len(soilToFert):
                if soilToFert[i][1] != soilToFert[i+1][0]:
                    sfmapped.append(soilToFert[i])
        
        addValue = newSoilToFert[soilToFert[posEnd]]
        sfmapped.append((soilToFert[posEnd][0]+addValue, s[1] + addValue))

print(sfmapped)

newFertToWater = newDicts[2]
fertToWater = ListOfmapRangeList[2]
fwmapped = []
for s in sfmapped:
    print(s)
    posStart = posWhereLess(s, fertToWater, 0)
    posEnd = posWhereLess(s, fertToWater, 1)
    
    if posStart == None and posEnd == None:
        fwmapped.append(s)
    elif posStart == None:
        addValue = newFertToWater[fertToWater[posEnd]]
        fwmapped.append((s[0] + addValue, s[1] + addValue))

    elif posStart-1 == posEnd:
        addValue = newFertToWater[fertToWater[posStart-1]]
        fwmapped.append((s[0]+addValue, s[1]+addValue))
    elif posStart >= posEnd:
        #ranges are: s[0], fertToWater[posEnd][1]
        #then a loop from posStart, posEnd
        # in this loop fertToWater[i][0], fertToWater[i][1]
        # and also check for any in between values with
        # fertToWater[i][1] != fertToWater[i+1][0] as long as i < len(fertToWater)
        # and if this is the case, range is (fertToWater[i][1], fertToWater[i+1][0])
        #then fertToWater[posEnd][0], s[1]
        addValue = newFertToWater[fertToWater[posStart-1]]
        fwmapped.append((s[0] + addValue, fertToWater[posEnd-1][1] + addValue))

        for i in range(posStart, posEnd):
            addValue = newFertToWater[fertToWater[i]]
            fwmapped.append((fertToWater[i][0] + addValue, fertToWater[i][1]))
            if i+1 < len(fertToWater):
                if fertToWater[i][1] != fertToWater[i+1][0]:
                    fwmapped.append(fertToWater[i])
        
        addValue = newFertToWater[fertToWater[posEnd]]
        fwmapped.append((fertToWater[posEnd][0]+addValue, s[1] + addValue))

print(fwmapped)

newWaterToLight = newDicts[3]
waterToLight = ListOfmapRangeList[3] 
wlmapped = []
for s in fwmapped:
    print(s)
    posStart = posWhereLess(s, waterToLight, 0)
    posEnd = posWhereLess(s, waterToLight, 1)
    
    if posStart == None and posEnd == None:
        wlmapped.append(s)
    elif posStart == None:
        addValue = newWaterToLight[waterToLight[posEnd]]
        wlmapped.append((s[0] + addValue, s[1] + addValue))
    
    elif posStart-1 == posEnd:
        addValue = newWaterToLight[waterToLight[posStart-1]]
        wlmapped.append((s[0]+addValue, s[1]+addValue))
    elif posStart >= posEnd:
        #ranges are: s[0], waterToLight[posEnd][1]
        #then a loop from posStart, posEnd
        # in this loop waterToLight[i][0], waterToLight[i][1]
        # and also check for any in between values with
        # waterToLight[i][1] != waterToLight[i+1][0] as long as i < len(waterToLight)
        # and if this is the case, range is (waterToLight[i][1], waterToLight[i+1][0])
        #then waterToLight[posEnd][0], s[1]
        addValue = newWaterToLight[waterToLight[posStart-1]]
        wlmapped.append((s[0] + addValue, waterToLight[posEnd-1][1] + addValue))

        for i in range(posStart, posEnd):
            addValue = newWaterToLight[waterToLight[i]]
            wlmapped.append((waterToLight[i][0] + addValue, waterToLight[i][1]))
            if i+1 < len(waterToLight):
                if waterToLight[i][1] != waterToLight[i+1][0]:
                    wlmapped.append(waterToLight[i])
        
        addValue = newWaterToLight[waterToLight[posEnd]]
        wlmapped.append((waterToLight[posEnd][0]+addValue, s[1] + addValue))

print(wlmapped)

newLightToTemp = newDicts[4]
lightToTemp = ListOfmapRangeList[4] 
print("Dict:", newLightToTemp)
ltmapped = []
for s in wlmapped:
    print(s)
    posStart = posWhereLess(s, lightToTemp, 0)
    posEnd = posWhereLess(s, lightToTemp, 1)
    
    if posStart == None and posEnd == None:
        ltmapped.append(s)
    elif posStart == None:
        addValue = newLightToTemp[lightToTemp[posEnd]]
        ltmapped.append((s[0] + addValue, s[1] + addValue))
    
    elif posStart-1 == posEnd:
        addValue = newLightToTemp[lightToTemp[posStart-1]]
        ltmapped.append((s[0]+addValue, s[1]+addValue))
    elif posStart >= posEnd:
        #ranges are: s[0], lightToTemp[posEnd][1]
        #then a loop from posStart, posEnd
        # in this loop lightToTemp[i][0], lightToTemp[i][1]
        # and also check for any in between values with
        # lightToTemp[i][1] != lightToTemp[i+1][0] as long as i < len(lightToTemp)
        # and if this is the case, range is (lightToTemp[i][1], lightToTemp[i+1][0])
        #then lightToTemp[posEnd][0], s[1]
        addValue = newLightToTemp[lightToTemp[posStart-1]]
        ltmapped.append((s[0] + addValue, lightToTemp[posEnd-1][1] + addValue))

        for i in range(posStart, posEnd):
            addValue = newLightToTemp[lightToTemp[i]]
            ltmapped.append((lightToTemp[i][0] + addValue, lightToTemp[i][1]))
            if i+1 < len(lightToTemp):
                if lightToTemp[i][1] != lightToTemp[i+1][0]:
                    ltmapped.append(lightToTemp[i])
        
        addValue = newLightToTemp[lightToTemp[posEnd]]
        ltmapped.append((lightToTemp[posEnd][0]+addValue, s[1] + addValue))

print(ltmapped)

newTempToHum = newDicts[5]
tempToHum = ListOfmapRangeList[5] 
print("Dict:", newTempToHum)
thmapped = []
for s in ltmapped:
    print(s)
    posStart = posWhereLess(s, tempToHum, 0)
    posEnd = posWhereLess(s, tempToHum, 1)
    
    if posStart == None and posEnd == None:
        thmapped.append(s)
    elif posStart == None:
        addValue = newTempToHum[tempToHum[posEnd]]
        thmapped.append((s[0] + addValue, s[1] + addValue))
    
    elif posStart-1 == posEnd:
        addValue = newTempToHum[tempToHum[posStart-1]]
        thmapped.append((s[0]+addValue, s[1]+addValue))
    elif posStart >= posEnd:
        #ranges are: s[0], tempToHum[posEnd][1]
        #then a loop from posStart, posEnd
        # in this loop tempToHum[i][0], tempToHum[i][1]
        # and also check for any in between values with
        # tempToHum[i][1] != tempToHum[i+1][0] as long as i < len(tempToHum)
        # and if this is the case, range is (tempToHum[i][1], tempToHum[i+1][0])
        #then tempToHum[posEnd][0], s[1]
        addValue = newTempToHum[tempToHum[posStart-1]]
        thmapped.append((s[0] + addValue, tempToHum[posEnd-1][1] + addValue))

        for i in range(posStart, posEnd):
            addValue = newTempToHum[tempToHum[i]]
            thmapped.append((tempToHum[i][0] + addValue, tempToHum[i][1]))
            if i+1 < len(tempToHum):
                if tempToHum[i][1] != tempToHum[i+1][0]:
                    thmapped.append(tempToHum[i])
        
        addValue = newTempToHum[tempToHum[posEnd]]
        thmapped.append((tempToHum[posEnd][0]+addValue, s[1] + addValue))

print("\n\n\n\n\n",thmapped)

newHumToLoc = newDicts[6]
humToLoc = ListOfmapRangeList[6] 
print("Dict:", newHumToLoc)
hlmapped = []
for s in thmapped:
    print(s)
    posStart = posWhereLess(s, humToLoc, 0)
    posEnd = posWhereLess(s, humToLoc, 1)
    
    if posStart == None and posEnd == None:
        hlmapped.append(s)
    elif posStart == None:
        addValue = newHumToLoc[humToLoc[posEnd]]
        hlmapped.append((s[0] + addValue, s[1] + addValue))
    elif posStart == -1 and posEnd != None:
        hlmapped.append(s[0], humToLoc[0][0])
        posStart = 0
    elif posStart == -1 and posEnd == None:
        hlmapped.append(s[0], humToLoc[0][0])
        posStart = 0
        posEnd = len(humToLoc) + 1
    elif posEnd == None:
        posEnd = len(humToLoc) + 1
    elif posStart-1 == posEnd:
        addValue = newHumToLoc[humToLoc[posStart-1]]
        hlmapped.append((s[0]+addValue, s[1]+addValue))
        
    elif posStart >= posEnd:
        #ranges are: s[0], humToLoc[posEnd][1]
        #then a loop from posStart, posEnd
        # in this loop humToLoc[i][0], humToLoc[i][1]
        # and also check for any in between values with
        # humToLoc[i][1] != humToLoc[i+1][0] as long as i < len(humToLoc)
        # and if this is the case, range is (humToLoc[i][1], humToLoc[i+1][0])
        #then humToLoc[posEnd][0], s[1]
        addValue = newHumToLoc[humToLoc[posStart-1]]
        hlmapped.append((s[0] + addValue, humToLoc[posEnd-1][1] + addValue))

        for i in range(posStart, posEnd):
            addValue = newHumToLoc[humToLoc[i]]
            hlmapped.append((humToLoc[i][0] + addValue, humToLoc[i][1]))
            if i+1 < len(humToLoc):
                if humToLoc[i][1] != humToLoc[i+1][0]:
                    hlmapped.append(humToLoc[i])
        
        addValue = newHumToLoc[humToLoc[posEnd]]
        hlmapped.append((humToLoc[posEnd][0]+addValue, s[1] + addValue))

print(hlmapped)