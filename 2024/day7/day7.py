import itertools

with open('data.txt') as f:
    data = [line.strip().split(': ') for line in f.readlines()]

answers, equations = [], []

for eq in data:
    answers.append(int(eq[0]))
    equations.append([int(num) for num in eq[1].split()])

operators = [0, 1]  # 0 is +, 1 is *
operation_combinations = []

num_satisfying = 0
for eq_idx in range(len(equations)):
    answer, equation = answers[eq_idx], equations[eq_idx]
    num_operators = len(equation) - 1
    combinations = itertools.product(operators, repeat = num_operators)
    flag = False
    for combination in combinations:
        result = equation[0]
        for i in range(len(combination)):
            if combination[i] == 0:
                result = result + equation[i+1]
            else:
                result = result * equation[i+1]
        
        if result == answer:
            flag = True
            break
    
    if flag:
        num_satisfying += answer

print(num_satisfying)

# Now, checking for each combination
# for i in range(len(answers)):
#     combinations = operation_combinations[i]
#     for combination in combinations:
#         result = 0
#         for i in range(len(combination)):
