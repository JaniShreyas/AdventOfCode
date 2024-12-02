with open('data.txt') as f:
    data = [[int(num) for num in line.split()] for line in f.readlines()]

def is_level_safe(level):
    inc, dec = 0, 0
    threshold = (1,3)
    thresh_flag = False
    for i in range(len(level) - 1):
        if level[i] < level[i+1]:
            inc = 1
        elif level[i] > level[i+1]:
            dec = 1
        if not (threshold[0] <= abs(level[i] - level[i+1]) <= threshold[1]):
            thresh_flag = True
            break
    
    if inc + dec == 2 or thresh_flag:
        return False
    return True

def get_safe_levels():
    safe = [False for _ in range(len(data))]

    for idx in range(len(data)):
        level = data[idx]

        if is_level_safe(level):
            safe[idx] = True

    return safe

def part1():
    print(sum(get_safe_levels()))

part1()

def part2():
    safe_levels = get_safe_levels()
    for idx in range(len(data)):
        one_safe_config = False
        if not safe_levels[idx]:
            # We try again by removing each element once
            base_level = data[idx]
            for i in range(len(base_level)):
                if is_level_safe(base_level[:i] + base_level[i+1:]):
                    one_safe_config = True
                    break
        
        if one_safe_config:
            safe_levels[idx] = True
    
    print(sum(safe_levels))

part2()