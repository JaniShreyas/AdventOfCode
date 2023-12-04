with open('data.txt') as  f:
    input = [line.strip() for line in f.readlines()]

listWinning = []
listElfs = []

sum = 0
for card in input:

    cardnum, numbers = card.split(': ')
    winning, elfs = numbers.split(' | ')

    winning = winning.split(' ')
    winning = [int(num.strip()) for num in winning if num != '']
    # print(winning)
    listWinning.append(winning)

    elfs = elfs.split(' ')
    elfs = [int(num.strip()) for num in elfs if num != '']
    # print(elfs)
    listElfs.append(elfs)

    n = 0
    for num in elfs:
        if num in winning:
            n += 1

    out = 2**(n-1)
    if n == 0:
        out = 0
    sum += out

# print(sum)

def numMatches(l1, l2):
    n = 0
    for num in l2:
        if num in l1:
            n += 1
    return n

def part2():
    l = [1 for i in range(len(input))]
    
    for i in range(len(input)):
        n = numMatches(listWinning[i], listElfs[i])
        
        if n != 0:
            for j in range(1, n+1):
                l[i+j] += l[i]

    sum = 0
    for num in l:
        sum += num
    
    return sum

from time import monotonic_ns

start = monotonic_ns()
part2()
end = monotonic_ns() - start
print(end)