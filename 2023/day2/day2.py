#12 red, 13 green, 14 blue
#We need to find all the games where the respective sums of each semicolon separated system was <= the max of each numbers

def part1():

    limit = {'red': 12, 'green': 13, 'blue': 14}

    validGames = []

    with open("data.txt") as f:
        lines = f.readlines()
        
        listOfMax = []

        for line in lines:
        
            #Separating game info from the games
            sep = line.split(':')
            id = int(sep[0][5:].strip())

            #Separating each instance from within a game
            allInstances = sep[1]
            eachInstance = allInstances.split(';')
            eachInstance[-1] = eachInstance[-1][:-1]

            #Removing leading white space
            for i in range(len(eachInstance)):
                eachInstance[i] = eachInstance[i][1:]
            

            #Need to maintain a dictionary which keeps track of max number of colors over each instance
            eachColor = []

            for i in range(len(eachInstance)):
                colorSets = eachInstance[i].split(',')
                eachColor.append(colorSets)

            for i in range(len(eachColor)):
                for j in range(1, len(eachColor[i])):
                    eachColor[i][j] = eachColor[i][j][1:]
            
            maximum = {'red': 0, 'green': 0, 'blue': 0}
            for i in range(len(eachColor)):
                for j in range(len(eachColor[i])):
                    color = eachColor[i][j][2:]
                    if color.endswith('red'):
                        red = int(eachColor[i][j][:2].strip())
                        if red > maximum['red']:
                            maximum['red'] = red
                    elif color.endswith('green'): 
                        green = int(eachColor[i][j][:2].strip())
                        if green > maximum['green']:
                            maximum['green'] = green
                    elif color.endswith('blue'):
                        blue = int(eachColor[i][j][:2].strip())
                        if blue > maximum['blue']:
                            maximum['blue'] = blue  

            flag = True
            for key in maximum.keys():
                if maximum[key] > limit[key]:
                    flag = False
                    break

            if(flag):
                validGames.append(id)  

            listOfMax.append(maximum)

    print(sum(validGames))
    return listOfMax

def part2():
    listOfMax = part1()
    sum = 0
    for m in listOfMax:
        power = 1
        for key in m.keys():
            power *= m[key]
        sum+= power
    
    return sum

print(part2())