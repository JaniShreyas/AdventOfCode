with open('data.txt') as f:
    data = [list(line.strip()) for line in f.readlines()]

rows, cols = len(data), len(data[0])

def add_indices(ind1, ind2):
    return (ind1[0] + ind2[0], ind1[1] + ind2[1])

def is_valid_index(ind):
    return (0 <= ind[0] < rows) and (0 <= ind[1] < cols)

region, perimeter = {}, {}
in_region = [[False for _ in range(cols)] for _ in range(rows)]

def find_region(current, parent):

    region[parent].append(current)
    in_region[current[0]][current[1]] = True

    hit = False
    perimeter_contribution = 0
    
    # Check all sides
    steps = [(0,1), (1,0), (0,-1), (-1,0)]

    for step in steps:
        new_point = add_indices(current, step)
        if new_point in region[parent]:
            continue
        if is_valid_index(new_point) and data[new_point[0]][new_point[1]] == data[current[0]][current[1]]:
            find_region(new_point, parent)
            hit = True
        else:
            perimeter_contribution += 1

    perimeter[parent] += perimeter_contribution

    
    if not hit:
        # No other path
        return




def part1():
    # Loop over all points
    # If they have been added in a region, continue
    # If not, send this to a recursive function which 
    # does recursion until all sides have a different letter
    # While all this, add their index to the region map with the parent index
    # Can parse the parent in parts later on, or just add the parent for ease

    for i in range(rows):
        for j in range(cols):
            if in_region[i][j]:
                continue
            region[(i,j)] = []
            perimeter[(i,j)] = 0
            find_region((i,j), (i,j))
    
    # Now to calculate area and perimeter
    # Area is simple, just the number of elements
    # For perimeter just add the number of non hits when doing DFS

    total = 0

    for r in region:
        total += len(region[r]) * perimeter[r]

    print(total)

part1()