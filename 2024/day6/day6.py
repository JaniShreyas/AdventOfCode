import copy

with open("data.txt") as f:
    data = [list(line.strip()) for line in f.readlines()]

faces = ['^', '>', 'v', '<']
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
num_faces = len(faces)
rows, cols = len(data), len(data[0])

guard, start_row, start_col = [(data[i][j], i, j) for j in range(cols) for i in range(rows) if data[i][j] in faces][0]

# This is the idea
# In an infinite loop, keep moving the guard's index in the step direction
# Before each move, check if the current / next character is one of 3 things
# If the current row is 0 and face is 0, or col is last and face is 1, or row is last and face is 2, or col is 0 and face is 3
# Then break out of loop
# If it is a '.', move forward
# If it is a '#', change direction by doing mod with num_faces after increment 
# After the latter 2 moves, add the reached index to a set. Since it is a set, it will automatically deal with duplicates

def patrol(area):
    global start_row, start_col
    index = faces.index(guard)
    row, col = start_row, start_col
    visited, turn_points = set(), list()
    visited.add((row, col))
    while True:

        if (row == 0 and index == 0) or (col == cols - 1 and index == 1) or (row == rows - 1 and index == 2) or (col == 0 and index == 3):
            break

        step = steps[index]
        next_row, next_col = row + step[0], col + step[1]

        if area[next_row][next_col] == '#':
            # Will hit obstacle, turn right
            if (row, col) in turn_points:
                return True, visited
            turn_points.append((row, col))
            index = (index + 1) % num_faces
            step = steps[index]
            next_row, next_col = row + step[0], col + step[1]
        

        row, col = next_row, next_col
        visited.add((row, col))
    return False, visited

def part1():
    print(len(patrol(data)[1]))

part1()

def part2():
    global start_row, start_col
    # First and most important thing to have is a function to detect loops, which can be done by saving the last 4 turning points
    # After this, I will run the part 1 function to get the points the guard will go over in its original path, and remove its starting point
    # Then, I will loop over all the positions, add a '#' at that spot, and run the is_loop function for that configuration
    _, on_route = patrol(data)
    on_route.remove((start_row, start_col))

    num_loops = 0
    for row, col in on_route:
        data_copy = copy.deepcopy(data)
        data_copy[row][col] = '#'
        if patrol(data_copy)[0]:
            num_loops += 1

    print(num_loops)

part2()