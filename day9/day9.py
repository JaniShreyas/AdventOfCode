with open("data.txt") as f:
    input = [line.strip() for line in f.readlines()]

input = [[int(num) for num in line.split(" ")] for line in input]


def nextVal(sequence, isPart1):
    if sequence == [0 for i in range(len(sequence))]:
        return 0

    diffSeq = []
    for i in range(len(sequence) - 1):
        diffSeq.append(sequence[i + 1] - sequence[i])

    return (
        sequence[-1] + nextVal(diffSeq, isPart1)
        if isPart1
        else sequence[0] - nextVal(diffSeq, isPart1)
    )

def sumNextVal(isPart1):
    nextVals = []
    for seq in input:
        nextVals.append(nextVal(seq, isPart1))
    print(sum(nextVals))

# True for part1, False for part2
sumNextVal(True)