with open('data.txt') as f:
    data = [list(line.strip()) for line in f.readlines()]

rows, cols = len(data), len(data[0])

def add_indices(ind1, ind2):
    return (ind1[0] + ind2[0], ind1[1] + ind2[1])

def is_valid_index(ind):
    return (0 <= ind[0] < rows) and (0 <= ind[1] < cols)

region, sides = {}, {}
in_region = [[False for _ in range(cols)] for _ in range(rows)]

def find_region_with_sides(current, parent, dir):
    
    region[parent].append(current)
    in_region[current[0]][current[1]] = True

    steps = [(0,1), (1,0), (0,-1), (-1,0)]

    flags = [False for _ in range(4)]
    child_flags_list = []

    for i in range(len(steps)):
        step = steps[i]
        new_point = add_indices(current, step)
        if new_point in region[parent]:
            continue
        if is_valid_index(new_point) and data[new_point[0]][new_point[1]] == data[current[0]][current[1]]:
            child_flags_list.append(find_region_with_sides(new_point, parent, i))
        else:
            flags[i] = True

    for child_flags in child_flags_list:
        for i in range(4):
            if child_flags[i] and not flags[i]:
                sides[parent] += 1

    if dir == -1:
        for flag in flags:
            if flag:
                sides[parent] += 1
            

    return flags


def part2():
    # If your direction is right, and you have a block on right, add 1 to sides
    # If your blockages don't match up with your direction, set their flag to True in a list 
    # If your childrens returned list of blocks doesn't match up with your blocks, there is a problem
    # Like if your child returned that it has a block in down and top, 
    # And you see you don't have a block down, you add 1 to sides, and set flag to False (satisified)
    # Maybe the end direction one can be merged

    # New version found
    # If your child's 4 return flags don't match yours, add 1 for each mismatch, then return your flags back
    # In the end this should cover all

    for i in range(rows):
        for j in range(cols):
            if in_region[i][j]:
                continue
            region[(i,j)] = []
            sides[(i,j)] = 0
            find_region_with_sides((i,j), (i,j), -1)

    print(region)
    print(sides)

part2()