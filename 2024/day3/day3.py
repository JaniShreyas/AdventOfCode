import re

with open("data.txt") as f:
    data = "".join(f.readlines())

def part1():
    commands = re.findall(r"mul\((\d+,\d+)\)", data)

    sum = 0
    for command in commands:
        first, last = command.split(',')
        sum += int(first) * int(last)

    print(sum)

# part1()

def part2():
    cur = 0
    result = ""
    enabled = True
    sum = 0
    while result is not None:
        result = re.search(r"do\(\)|don't\(\)|mul\((\d+,\d+)\)", data[cur:])
        if result is None:
            break
        res = result.group()
        if res == "do()":
            enabled = True
        elif res == "don't()":
            enabled = False
        elif enabled:
            sum += multiply(res)
        cur += result.end()
    
    print(sum)

def multiply(res: str):
    instruction = res[4:-1]
    first, last = [int(x) for x in instruction.split(',')]
    return first*last

part2()