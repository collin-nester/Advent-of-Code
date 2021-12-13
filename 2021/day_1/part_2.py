#Advent of Code 2021 Day 1 Part 1

with open('/Users/collinnester24/Documents/python/advent_of_code/2021/day_1/input.txt', 'r') as reader:
    depth_list = reader.readlines()

increases = 0
for i, j in enumerate(depth_list):
    if i > 2:
        if int(j) > int(depth_list[ i - 3 ]):
            increases += 1
print(increases)