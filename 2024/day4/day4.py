from time import monotonic_ns

start = monotonic_ns()

with open("data.txt") as f:
    data = [line.strip() for line in f.readlines()]

# And you know what why was I overcomplicating this shit.
# All I have to do is check all the points for all X's

rows, cols = len(data), len(data[0])

def part1():
    xmas = 'XMAS'

    def find_right(i, j):
        if j > cols - 4:
            return None
        return data[i][j:j+4]  

    def find_bottom_right(i,j):
        if i > rows - 4 or j > cols - 4:
            return None
        word = ""
        for diag in range(4):
            word += data[i+diag][j+diag]
        return word

    def find_bottom(i,j):
        if i > rows - 4:
            return None
        word = ""
        for row in range(4):
            word += data[i+row][j]
        return word

    def find_bottom_left(i,j):
        if i > rows - 4 or j < (len(xmas) - 1):
            return None
        word = ""
        for diag in range(4):
            word += data[i+diag][j-diag]
        return word

    def find_left(i,j):
        if j < (len(xmas) - 1):
            return None
        return (data[i][j-3:j+1])[::-1]

    def find_top_left(i,j):
        if i < (len(xmas) - 1) or j < (len(xmas) - 1):
            return None
        word = ""
        for diag in range(4):
            word += data[i-diag][j-diag]
        return word

    def find_top(i,j):
        if i < (len(xmas) - 1):
            return None
        word = ""
        for row in range(4):
            word += data[i-row][j]
        return word

    def find_top_right(i,j):
        if i < (len(xmas) - 1) or j > cols - 4:
            return None
        word = ""
        for diag in range(4):
            word += data[i-diag][j+diag]
        return word

    def find_all_dir(i,j):
        zero = find_right(i,j)
        one = find_bottom_right(i,j)
        two = find_bottom(i,j)
        three = find_bottom_left(i,j)
        four = find_left(i,j)
        five = find_top_left(i,j)
        six = find_top(i,j)
        seven = find_top_right(i,j)

        return [zero, one, two, three, four, five, six, seven]

    xmas_count = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != 'X':
                continue
            hits = find_all_dir(i,j)
            for hit in hits:
                if hit is not None and hit == xmas:
                    xmas_count += 1

    print(xmas_count)

part1()

def part2():
    # In this one, once we have found an A, we need to check for 2 diagonal strings
    # And if both of them are either MAS or SAM, we increment the count

    # Diagonal going from top left to bottom right
    def upper_left(i,j):
        row, col = i-1, j-1
        word = ""
        for diag in range(3):
            word += data[row+diag][col+diag]
        return word

    # Diagonal going from bottom left to top right
    def upper_right(i,j):
        row, col = i+1, j-1
        word = ""
        for diag in range(3):
            word += data[row-diag][col+diag]
        return word
    
    count = 0
    # Since there is no case where an X-MAS can be in the 0th row or col, we start from index 1 till row-1 and col-1
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if data[i][j] != 'A':
                continue
            ul = upper_left(i,j)
            ur = upper_right(i,j)
            mas = ['SAM', 'MAS']
            if (ul in mas) and (ur in mas):
                count += 1
    
    print(count)

part2()

print(monotonic_ns() - start)