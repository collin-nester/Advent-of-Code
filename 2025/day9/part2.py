import copy
import numpy as np
import bitarray
import pprint

with open("2025/day9/input.txt", "r") as reader:
    input = reader.readlines()

coord_list = []
for i in input:
    coord = [int(i.split(",")[1]), int(i.split(",")[0])]
    coord_list.append(coord)

def is_valid(first_coord_index, second_coord_index, coord_list):
    first_coord = coord_list[first_coord_index]
    second_coord = coord_list[second_coord_index]
    same_side = False
    if (first_coord[0] >= 50025 and second_coord[0] >= 50025) or (first_coord[0] <= 48753 and second_coord[0] <= 48753) or (first_coord[1] >= 94870 and second_coord[1] >= 94870):
        same_side = True
    neighbor_collision = False
    for coord in coord_list:
        if (coord[0] > first_coord[0] and coord[0] < second_coord[0]) or (coord[0] < first_coord[0] and coord[0] > second_coord[0]):
            if (coord[1] > first_coord[1] and coord[1] < second_coord[1]) or (coord[1] < first_coord[1] and coord[1] > second_coord[1]):
                neighbor_collision = True
                return False
    return same_side and not neighbor_collision

largest = 0
for first_coord_index, first_coord in enumerate(coord_list):
    for second_coord_index, second_coord in enumerate(coord_list[first_coord_index+1:]):
        second_coord_index += first_coord_index + 1
        if is_valid(first_coord_index, second_coord_index, coord_list):
            if (abs(first_coord[0] - second_coord[0]) + 1) * (abs(first_coord[1] - second_coord[1]) + 1) > largest:
                print(first_coord)
                print(second_coord)
                print()
                largest = max(largest, (abs(first_coord[0] - second_coord[0]) + 1) * (abs(first_coord[1] - second_coord[1]) + 1))

print(largest)