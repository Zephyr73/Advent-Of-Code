with open('2024/1/input.txt', 'r') as f:
    lines = f.readlines()

left_list = []
right_list = []
total = 0
similar_list = []
similarity_score = 0

for x in range(len(lines)): #['x y']
    line = lines[x].strip().split() #['x', 'y']
    for y in range(len(line)):
        line[y] = int(line[y])
    lines[x] = line

for pair in lines:
    left_list.append(pair[0])
    right_list.append(pair[1])

for x in range(len(lines)):
    total = total + abs(sorted(left_list)[x] - sorted(right_list)[x])

print(total) # Answer for Part 1

for x in range(len(lines)):
    similar = 0
    for y in range(len(lines)):
        if left_list[x] == right_list[y]:
            similar = similar + 1
    
    similar_list.append([left_list[x], similar])

for x in range(len(similar_list)):
    similarity_score = similarity_score + (similar_list[x][1] * similar_list[x][0])

print(similarity_score) # Answer for Part 2