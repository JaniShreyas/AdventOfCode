from time import monotonic_ns
start = monotonic_ns()

with open('data.txt') as f:
    data = f.readline().split()

def blink(stones: list[str]) -> list[str]:
    new_stones = []
    for i in range(len(stones)):
        stone = stones[i]
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            nh = len(stone) // 2
            first, second = stone[:nh], stone[nh:]
            if second == '0' * nh:
                second = '0'
            else:
                second = second.lstrip('0')
            new_stones.extend([first, second])
        else:
            new_stones.append(str(int(stone) * 2024))
    
    return new_stones


def part1():
    num_blinks = 25
    stones = data
    for _ in range(num_blinks):
        new_stones = blink(stones) 
        # print(new_stones) 
        stones = new_stones
    # print(new_stones)
    print(len(new_stones))     

part1()

print(monotonic_ns() - start)