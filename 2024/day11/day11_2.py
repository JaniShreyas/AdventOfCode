from time import monotonic_ns
from functools import cache

start = monotonic_ns()

with open('data.txt') as f:
    data = f.readline().split()

print(data)

# Some kind of iterative memoization recursion?

def get_new_stones(stone: str) -> list[str]:
    if stone == '0':
        return ['1']
    elif len(stone) % 2 == 0:
        nh = len(stone) // 2
        first, second = stone[:nh], stone[nh:]
        if second == '0' * nh:
            second = '0'
        else:
            second = second.lstrip('0')
        return [first, second]
    else:
        return [str(int(stone) * 2024)]

@cache
def blink_stone(stone: str, level: int, end: int) -> int:
    if level == end:
        return 1
    
    new_stones = get_new_stones(stone)
    score = 0
    for new_stone in new_stones:
        score += blink_stone(new_stone, level + 1, end)
    
    return score

    

def part2():
    total = 0
    num_blinks = 75
    for stone in data:
        total += blink_stone(stone, 0, num_blinks)
    print(total)

part2()

# print(monotonic_ns() - start)