file = open('D:/Programming/Python/Advent Of Code/2020/list1.txt', 'r')
data = []
for x in file:
    data.append(int(x))

#part 1
for x in data:
    for y in data:
        if x + y == 2020:
            prod = x*y
            break
#part 2
for x in data:
    for y in data:
        for z in data:
            if x + y + z == 2020:
                prod2 = x*y*z
                break
print (prod)
print (prod2)