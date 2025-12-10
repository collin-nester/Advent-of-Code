import copy
import numpy as np

with open("2025/day9/input.txt", "r") as reader:
    input = reader.readlines()

coord_list = []
for i in input:
    coord = [int(i.split(",")[0]), int(i.split(",")[1])]
    coord_list.append(coord)

largest = 0
for first_coord_index, first_coord in enumerate(coord_list):
    for second_coord_index, second_coord in enumerate(coord_list[first_coord_index+1:]):
        largest = max(largest, (abs(first_coord[0] - second_coord[0]) + 1) * (abs(first_coord[1] - second_coord[1]) + 1))

print(largest)