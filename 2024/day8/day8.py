with open('data.txt') as f:
    data = [list(line.strip()) for line in f.readlines()]

# Take each non '.' element as a key
# And a list of the indices they are at as values
antennas = {}
rows, cols = len(data), len(data[0])

for i in range(rows):
    for j in range(cols):
        if data[i][j] == '.':
            continue
        
        antenna = data[i][j]
        if antenna in antennas:
            antennas[antenna].append((i,j))
        else:
            antennas[antenna] = [(i,j)]

def is_valid_index(index):
    return 0 <= index[0] < rows and 0 <= index[1] < cols

# Loop through in a combination manner and find the respective antinode indices
# Increment antinode counter if the index is valid

def part1():
    anti_count_set = set()

    for freq in antennas:
        locations = antennas[freq]
        for i in range(len(locations) - 1):
            loc1 = locations[i]
            for j in range(i+1, len(locations)):
                loc2 = locations[j]
                
                # Find difference as loc1 - loc2
                diff = (loc1[0] - loc2[0], loc1[1] - loc2[1])
                
                # For one antinode, add diff to loc1
                # For the other subtract diff from loc2
                anti1 = (loc1[0] + diff[0], loc1[1] + diff[1])
                anti2 = (loc2[0] - diff[0], loc2[1] - diff[1])

                if is_valid_index(anti1):
                    anti_count_set.add(anti1)
                if is_valid_index(anti2):
                    anti_count_set.add(anti2)

    print(len(anti_count_set))

part1()

def step_index(index, step, direction = 1):
    return (index[0] + direction * step[0], index[1] + direction * step[1])

def part2():
    # Now, when I get the step, there are 2 locations added for each of those antennae obv
    # Other than this, I can run a while loop for 2 sides calculating the index and adding it
    # If it is a valid index

    anti_count_set = set()

    for freq in antennas:
        locations = antennas[freq]
        for i in range(len(locations) - 1):
            loc1 = locations[i]
            for j in range(i+1, len(locations)):
                loc2 = locations[j]
                
                # Find difference as loc1 - loc2
                diff = (loc1[0] - loc2[0], loc1[1] - loc2[1])

                possible_anti_node_index = loc1
                while is_valid_index(possible_anti_node_index):
                    anti_count_set.add(possible_anti_node_index)
                    possible_anti_node_index = step_index(possible_anti_node_index, diff, direction = 1)
                
                possible_anti_node_index = loc2
                while is_valid_index(possible_anti_node_index):
                    anti_count_set.add(possible_anti_node_index)
                    possible_anti_node_index = step_index(possible_anti_node_index, diff, direction = -1)
    
    print(len(anti_count_set))

part2()