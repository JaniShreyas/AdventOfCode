from functools import cmp_to_key

with open("data.txt") as f:
    rules, sequences = [[s for s in section.split('\n')] for section in f.read().split('\n\n')]

sequences = [seq.split(',') for seq in sequences]


# Okay, so the approach is to create a before dictionary where the key is a number,
# And the value is a list of numbers which are supposed to before that number in a sequence

# When going through a sequence, for each number, we will check its following numbers,
# And if any number is supposed to be before it according to the rule, we flag and break

# Creating the dictionary

greater_than = {}
for rule in rules:
    before, after = rule.split('|')
    if after in greater_than:
        greater_than[after].append(before)
    else:
        greater_than[after] = [before]

# Just checking if all elements have some relation defined
# unique_pages = {}
# for seq in sequences:
#     for page in seq:
#         if page not in unique_pages:
#             unique_pages[page] = False

# for key in greater_than:
#     if key in unique_pages:
#         unique_pages[key] = True
#     for val in greater_than[key]:
#         if val in unique_pages:
#             unique_pages[val] = True

# for key in unique_pages:
#     if not unique_pages[key]:
#         print("found an imposta")

# Turns out each page has some relation defined with another page
# This doesn't necessarily tell us that all pages have a relation defined with all other pages though
# But from what I can see there are exactly 6 instances of all numbers defined in the example data
# So I am going to assume that that is indeed the case with the actual data and find out :D

def get_incorrect_sequences(sequences):
    indices = [False for _ in range(len(sequences))]
    for idx in range(len(sequences)):
        seq = sequences[idx]
        flag = False
        for i in range(len(seq)):
            try:
                before_list = greater_than[seq[i]]
            except:
                continue
            for j in range(i+1, len(seq)):
                if seq[j] in before_list:
                    flag = True
                    break
            
            if flag:
                break
        if flag:
            indices[idx] = True
    
    return indices

incorrect_sequences = get_incorrect_sequences(sequences)

def find_median(seq):
        return int(seq[len(seq)//2])    

def part1():

    median_sum = 0
    for i in range(len(sequences)):
        if not incorrect_sequences[i]:
            median_sum += find_median(sequences[i])

    print(median_sum)

# part1()

def part2():
    # I had though of this while in part1 but didn't need it but this _is_ a sorting question with a look up table for less than
    # So I just make a less than table (dictionary) and sort based on that
    # pretty easy
    # need to set up a comparer for the sorted function

    def compare_pages(page1: str, page2: str) -> int:
        if page1 == page2:
            return 0
        
        try:
            if page2 in greater_than[page1]:
                return 1
        except:
            pass

        return -1
    
    median_sum = 0
    for idx in range(len(sequences)):
        if incorrect_sequences[idx]:
            # Sort and then add median to sum
            sorted_seq = sorted(sequences[idx], key = cmp_to_key(compare_pages))
            # print(sorted_seq)
            median_sum += find_median(sorted_seq)

    print(median_sum)

part2()