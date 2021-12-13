#Advent of Code day 2 part 1

with open('/Users/collinnester24/Documents/python/advent_of_code/2021/day_2/input.txt', 'r') as reader:
    directions = reader.readlines()

hor = 0
depth = 0
print(directions)
for i in directions:
    i = i.replace('\n', '')
    print(i)
    if 'forward' in i:
        hor += int(i[-1])
    elif 'up' in i:
        depth -= int(i[-1])
    elif 'down' in i:
        depth += int(i[-1])
print(hor * depth)