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

part1()