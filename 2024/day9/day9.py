with open('data.txt') as f:
    data = [int(p) for p in ''.join(f.readlines())]

# If index is even, it is memory block
# If index is odd, it is free space

# I could hypothetically, recreate the manual algorithm described in the problem
# With the opening, and then slowly going through it all
# And this does seem more feasible even

# Or there could be a more clever approach with while loops
# Hmm, the first approach seems better, lets go with that

# Find the IDs of all the processes and convert to the expanded form simulataneously

def get_expanded_processes():
    expanded_processes = []
    id = 0
    for i in range(len(data)):
        if i % 2 == 0:
            # Process
            for count in range(data[i]):
                expanded_processes.append(str(id))
            id += 1

        else:
            # Free space
            for count in range(data[i]):
                expanded_processes.append('.')
    
    return expanded_processes

# Calculate the hash
def checksum(expanded_processes):
    hash = 0
    for i in range(len(expanded_processes)):
        if expanded_processes[i] == '.':
            continue
        hash += i * int(expanded_processes[i])

    print(hash)

def part1():
    # Use 2 pointers, one for free space, one for last memory block
    # And fill in each space

    expanded_processes = get_expanded_processes()

    free_index, last_process_index = 0, len(expanded_processes) - 1
    while True:
        while expanded_processes[free_index] != '.':
            free_index += 1
        
        while expanded_processes[last_process_index] == '.':
            last_process_index -= 1
        
        if free_index > last_process_index:
            break
        
        # Swap the 2 values
        expanded_processes[free_index], expanded_processes[last_process_index] = expanded_processes[last_process_index], expanded_processes[free_index]
    checksum(expanded_processes)

part1()

def part2():
    # Now, I can either again try to do some other shit with dealing with the whole numbers
    # Or I can try something like, looping from the back with 2 pointers describing the start and end of the same ID process
    # Then when I have found this process and its length, I will search for free space start and end indices with that many dots
    # Alright, second one it is

    expanded_processes = get_expanded_processes()

    # Have 2 pointers showing the index of the block of processes to shift
    # Check from the start for free space points
    # If any consecutive free spaces with same length as the processes
    # Swap them
    # Move the pointers whether found or not
    # Always stop the free space search before the start index of the process to be checked

    n = len(expanded_processes)
    pstart, pend = n - 1, n

    while True:
        # Move pstart down until a different ID in the lower down block or pstart == 0
        while pstart > 0 and (expanded_processes[pstart] == expanded_processes[pstart - 1] or expanded_processes[pstart] == '.'):
            pstart -= 1

        # pend will initially be n given the data, but it will be updated to pstart (and pstart decremented after) to check with the next starting points
        # It can happen that there are dots between pstart and pend so will loop until that is fixed

        while expanded_processes[pend - 1] == '.':
            pend -= 1

        if pend <= 0:
            break

        process_len = pend - pstart

        print(pstart, pend)

        # After this, we start a loop to search for free spaces, and keep track of consecutive spaces
        fstart, fend = 0, 1  # Since this is the earliest free space can be
        found_space = False

        while True:

            # Find closest dot
            while expanded_processes[fstart] != '.':
                fstart += 1

            # If fstart is ever greater than pstart we are at a bad point
            if fstart >= pstart:
                break

            fend = fstart + 1

            # Find end of dots
            while expanded_processes[fend] == '.':
                fend += 1

            # Now I have the free stuff
            # Check if this is enough to keep the process block
            if fend - fstart >= process_len:
                # Yes it is, so set off a flag
                found_space = True
                break
            else:
                # Keep searching further
                fstart = fend
                fend += 1
        
        # If I have found some space, swap the blocks
        if found_space:
            expanded_processes[pstart: pend], expanded_processes[fstart: fstart + process_len] = expanded_processes[fstart: fstart + process_len], expanded_processes[pstart: pend]

        # Else, don't do anything
        # After this, move the pend pointer down to pstart, and decrement pstart
        pend = pstart
        pstart -= 1

    checksum(expanded_processes)


part2()