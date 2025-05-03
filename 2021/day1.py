file = open("D://Programming/Python/Advent Of Code/2021/list1.txt", 'r')
increased = 0
prev = None

for x in file:
    if prev is None:
        prev = x
    if x > prev:
        increased += 1
    prev = x

print (increased)