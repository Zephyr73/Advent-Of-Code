safe = 0
levels_list = []

# Function to check if the levels are safe
# A level is safe if the difference between consecutive levels is between 1 and 3 (inclusive)
# and the levels are either strictly increasing or strictly decreasing
# The function checks the difference between each pair of consecutive levels
# If the difference is not between 1 and 3, it returns False
# If the levels are strictly increasing or strictly decreasing while the difference is between 1 and 3, it returns True

def is_safe(levels):
    increasing = True
    decreasing = True

    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if not (1 <= diff <= 3):
            return False

        if levels[i] < levels[i + 1]:
            decreasing = False
        elif levels[i] > levels[i + 1]:
            increasing = False

    return increasing or decreasing

# Read the input file and convert to list of integers
# 'levels' look like '1 2 3 4 5\n', '6 7 8 9 10\n', etc.
# 'level.strip().split()' converts to ['1', '2', '3', '4', '5']
# 'levels_list' looks like [['1', '2', '3', '4', '5'], ['6', '7', '8', '9', '10']]
# 'levels_list[x][y]' converts to int, so 'levels_list' looks like [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

with open('d:/Programming/Python/Advent Of Code/2024/2/input.txt', 'r') as f:
    levels = f.readlines()
    for level in levels:
        levels_list.append(level.strip().split())
        for x in range(len(levels_list)):
            for y in range (len(levels_list[x])):
                levels_list[x][y] = int(levels_list[x][y])

# 'level' in 'levels_list' looks like [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], etc.
# if a 'level' is increasing or decreasing, 'is_safe' returns True

for level in levels_list:
    if is_safe(level):
        safe += 1

print(safe) # Answer for part 1


# for each 'level' in 'levels_list', if it is not safe, it pops the first element and checks if it is safe
# if it is safe, it adds 1 to 'safe' and breaks the loop
# if it is not safe, it pops the second element and checks if it is safe

for level in levels_list:
    if not is_safe(level):
        for i in range(len(level)):
            popped = level.pop(i)
            if is_safe(level):
                safe += 1
                break
            else:
                level.insert(i, popped)
        
print (safe) # Answer for part 2