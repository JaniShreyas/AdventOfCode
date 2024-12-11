with open('data.txt') as f:
    data = [[int(num) for num in list(line.strip())] for line in f.readlines()]

# Right, down, left, up
steps = [(0,1), (1,0), (0,-1), (-1,0)]

def add_indices(ind1, ind2):
    return (ind1[0] + ind2[0], ind1[1] + ind2[1])

rows, cols = len(data), len(data[0])
unique_nines = set()

def find_trails(pos, trailhead) -> int:
    # Check all 4 sides for values exactly one more than current
    # Recursively call this function until base condition of current = 9 or ending in the loop only with next = 9. Probably latter if first is slow

    current = data[pos[0]][pos[1]]
    if current == 9:
        unique_nines.add((trailhead, pos))
        return 1
    
    score = 0
    for step in steps:
        next_ind = add_indices(pos, step)
        if next_ind[0] < 0 or next_ind[1] < 0 or next_ind[0] >= rows or next_ind[1] >= cols:
            continue
        if data[next_ind[0]][next_ind[1]] == current + 1:
            # Good
            score += find_trails(next_ind, trailhead)
    return score

def part1():
    total_score = 0
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == 0:
                total_score += find_trails((i,j), (i,j))

    print("Part 1", len(unique_nines))
    print("Part 2", total_score)

part1()