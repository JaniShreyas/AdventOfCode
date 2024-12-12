from typing import List, Set, Optional

with open("data.txt") as f:
    data = [list(line.strip()) for line in f.readlines()]

faces = ['^', '>', 'v', '<']

steps = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

rows, cols = len(data), len(data[0])

def patrol(area: List[List[str]], face_index: int, start_index: tuple[int, int], num_faces: int, changed_point: tuple[int, int] | None = None) -> tuple[bool, Optional[Set[tuple[int, int]]]]:

    # Given an area, do an infinite loop and keep moving the guard in the direction of his face
    row, col = start_index[0], start_index[1]
    visited = set()
    turn_points = []

    # if changed_point is not None:
    #     print(f"\n\n\n {changed_point} \n\n\n")
    while True:
        visited.add((row, col))
        # If on the edge rows or columns with relevant face of guard, break out of loop and return False outside
        if (row == 0 and face_index == 0) or (row == rows - 1 and face_index == 2) or (col == 0 and face_index == 3) or (col == cols - 1 and face_index == 1):
            break

        # Check the next possible position for obstacle, and rotate if yes
        # While rotating, add this point where rotation was done to a turn_points list
        # Before this rotation, check if this point is already in turn_points, and if yes, we have ourselves a loop
        # In this case, return with True, and visited
        step = steps[face_index]
        # next_row, next_col = row + step[0], col + step[1]

        # print(row, col, face_index)
        if area[row + step[0]][col + step[1]] == '#':
            # Check if already in 1
            if (row, col) in turn_points:
                return True, None
            
            # Add if not in
            turn_points.append((row, col))

            # Rotate
            face_index = (face_index + 1) % num_faces

            # Update next_row, next_col
            step = steps[face_index]  # Might be potential problem if wrong answer
        
        if area[row + step[0]][col + step[1]] == '#':
            # God damn this edge case socha kyun nahi
            face_index = (face_index + 1) % num_faces
            step = steps[face_index]

        next_row, next_col = row + step[0], col + step[1]

        row, col = next_row, next_col
    
    return False, visited

def main():
    # Find guard's face direction
    guard, start_index = [(data[i][j], (i,j)) for j in range(cols) for i in range(rows) if data[i][j] in faces][0]
    face_index = faces.index(guard)
    num_faces = len(faces)
    # print(face_index, start_index)

    # Get all points on path
    is_loop, path_points = patrol(data, face_index, start_index, num_faces)
    if path_points == None:
        raise Exception("Something went really wrong if there is a loop found in the base data")
    
    # Remove start index from visited points
    path_points.remove(start_index)

    num_loop_pos = 0
    # Loop over all path points
    for point in path_points:
        
        # Add an obstacle to this point
        data[point[0]][point[1]] = '#'

        # Send this data to patrol
        is_loop, _ = patrol(data, face_index, start_index, num_faces, point)

        # If it returns is_loop, append the loop counter
        if is_loop:
            num_loop_pos += 1

        # Reset this index to be '.'
        data[point[0]][point[1]] = '.'

    print(num_loop_pos)

main()