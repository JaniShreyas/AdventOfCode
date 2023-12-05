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

# alright, now I have the maps with the range of source as keys and range of destination as values
# now I beed to search through all the seed numbers, find their map to fertilizer, then that ferilizers map to water, and so on until location
# and save it as {seed: location}
# then find the key with minimum value
#should be easy

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

        if s in range(start, end):
            j = s - start
            seedS[s] = startVal+j
            isInRange = True

        # for j in range(end - start):
        #     if s == start + j:
        #         # if seed number is equal to this value, then find and save the corresponding value
        #         seedS[s] = startVal+j
        #         isInRange = True
        
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

        if val in range(start, end):
            j = val-start
            soilF[val] = startVal+j
            isInRange = True

        # for j in range(end - start):
        #     if val == start + j:
        #         # if seed number is equal to this value, then find and save the corresponding value
        #         soilF[val] = startVal+j
        #         isInRange = True
        
    if not isInRange:
        soilF[val] = val

for val in soilF.values():
    fToWKeys = list(fertilizerToWaterDict.keys())
    fToWValues = list(fertilizerToWaterDict.values())
    
    isInRange = False
    for i in range(len(fToWKeys)):
        start, end = fToWKeys[i]
        startVal, endVal = fToWValues[i]

        if val in range(start, end):
            j = val-start
            fW[val] = startVal+j
            isInRange = True

        # for j in range(end - start):
        #     if val == start + j:
        #         # if seed number is equal to this value, then find and save the corresponding value
        #         fW[val] = startVal+j
        #         isInRange = True
        
    if not isInRange:
        fW[val] = val

for val in fW.values():
    wToLKeys = list(waterToLightDict.keys())
    wToLValues = list(waterToLightDict.values())
    
    isInRange = False
    for i in range(len(wToLKeys)):
        start, end = wToLKeys[i]
        startVal, endVal = wToLValues[i]

        if val in range(start, end):
            j = val-start
            wL[val] = startVal+j
            isInRange = True

        # for j in range(end - start):
        #     if val == start + j:
        #         # if seed number is equal to this value, then find and save the corresponding value
        #         wL[val] = startVal+j
        #         isInRange = True
        
    if not isInRange:
        wL[val] = val

for val in wL.values():
    lToTKeys = list(lightToTemperatureDict.keys())
    lToTValues = list(lightToTemperatureDict.values())
    
    isInRange = False
    for i in range(len(lToTKeys)):
        start, end = lToTKeys[i]
        startVal, endVal = lToTValues[i]

        if val in range(start, end):
            j = val-start
            lT[val] = startVal+j
            isInRange = True

        # for j in range(end - start):
        #     if val == start + j:
        #         # if seed number is equal to this value, then find and save the corresponding value
        #         lT[val] = startVal+j
        #         isInRange = True
        
    if not isInRange:
        lT[val] = val

for val in lT.values():
    tToHKeys = list(temperatureToHumidityDict.keys())
    tToHValues = list(temperatureToHumidityDict.values())
    
    isInRange = False
    for i in range(len(tToHKeys)):
        start, end = tToHKeys[i]
        startVal, endVal = tToHValues[i]

        if val in range(start, end):
            j = val-start
            tH[val] = startVal+j
            isInRange = True

        # for j in range(end - start):
        #     if val == start + j:
        #         # if seed number is equal to this value, then find and save the corresponding value
        #         tH[val] = startVal+j
        #         isInRange = True
        
    if not isInRange:
        tH[val] = val

for val in tH.values():
    hToLKeys = list(humidityToLocationDict.keys())
    hToLValues = list(humidityToLocationDict.values())
    
    isInRange = False
    for i in range(len(hToLKeys)):
        start, end = hToLKeys[i]
        startVal, endVal = hToLValues[i]

        if val in range(start, end):
            j = val-start
            hL[val] = startVal+j
            isInRange = True

        # for j in range(end - start):
        #     if val == start + j:
        #         # if seed number is equal to this value, then find and save the corresponding value
        #         hL[val] = startVal+j
        #         isInRange = True
        
    if not isInRange:
        hL[val] = val

loc = []
for s in seed:
    l = hL[tH[lT[wL[fW[soilF[seedS[s]]]]]]]
    loc.append(l)

print(min(loc))