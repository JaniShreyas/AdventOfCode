import re

with open("data.txt") as f:
    time = f.readline()
    distance = f.readline()

digits = []
m = re.finditer(r"(\d+)", time)
for match in m:
    s = int(match.start())
    e = int(match.end())
    num = time[s:e]
    digits.append(int(num))

dist = []
m = re.finditer(r"(\d+)", distance)
for match in m:
    s = int(match.start())
    e = int(match.end())
    num = distance[s:e]
    dist.append(int(num))


def part1():
    countList = []
    for i in range(len(digits)):
        time = digits[i]
        count = 0
        chargeTime = 0
        for j in range(time+1):
            d = j * (time - j)
            if d > dist[i]:
                count += 1
        countList.append(count)

    prod = 1
    for c in countList:
        prod *= c
    print(prod)


def part2():
    s = ""
    for t in digits:
        s += str(t)

    t = int(s)

    s = ""
    for d in dist:
        s += str(d)

    d = int(s)

    count = 0
    for j in range(t+1):
        g = j * (t - j)
        if g > d:
            count += 1

    print(count)

part1()
part2()