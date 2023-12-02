from time import monotonic

#Need to 
#1. Read line
#2. find the numbers in the line 
#3. Add them to a rolling sum

def part1():
    
    sum = 0

    with open("data.txt") as f:
        lines = f.readlines()
        for line in lines:

            num = ''

            for char in line:
                if char.isnumeric():
                    num += char
                    break
            
            for i in range(len(line) - 1, -1, -1):
                if line[i].isnumeric():
                    num += line[i]
                    break

            sum += int(num)
    
    print(sum)

def part2():

    sum = 0

    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    with open("data.txt") as f:
        lines = f.readlines()
        
        for line in lines:

            res = ''
            num = ''

            #forward
            for char in line:
                if char.isnumeric():
                    num += char
                    break
                res += char

                flag = False
                for n in numbers.keys():
                    if n in res:
                        num += str(numbers[n])
                        flag = True
                        break
                if(flag):
                    break
            # print(num)
            
            #backward
            res = ''
            for i in range(len(line) - 1, -1, -1):
                char = line[i]
                if char.isnumeric():
                    num += char
                    break
                res += char
                rev = res[::-1]

                flag = False
                for n in numbers.keys():
                    if n in rev:
                        num += str(numbers[n])
                        flag = True
                        break
                
                if(flag):
                    break
            
            sum += int(num)

    print(sum)

part1()