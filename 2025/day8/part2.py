import copy
import numpy as np

with open("2025/day8/input.txt", "r") as reader:
    input = reader.readlines()

box_coords = []
for line in input:
    box_coords.append(line.strip().split(","))
    for i, coord in enumerate(box_coords[-1]):
        box_coords[-1][i] = int(coord)

def dist_btwn(box_coords1, box_coords2):
    return pow(pow(box_coords1[0]-box_coords2[0],2)+pow(box_coords1[1]-box_coords2[1],2)+pow(box_coords1[2]-box_coords2[2],2), 0.5)

distance_between = np.zeros((len(box_coords),len(box_coords)))
for first, box_coords1 in enumerate(box_coords):
        for second, box_coords2 in enumerate(box_coords):
            dist = dist_btwn(box_coords1, box_coords2)
            distance_between[first][second] = dist

print("Distances Calculated")

ordered_circuits_increasing_distance = [10000000]
ordered_circuits_locations = [[999999, 999999]]
for first, box_coords1 in enumerate(box_coords):
    print(str(first) + " Boxes Sorted")
    for second, box_coords2 in enumerate(box_coords[first+1:]):
        second += first + 1
        index_not_found = True
        low = 0
        high = len(ordered_circuits_increasing_distance)
        pair_distance = distance_between[first][second]
        while index_not_found:
            mid = int((low + high) / 2)
            if high <= low:
                index_not_found = False
            elif pair_distance < ordered_circuits_increasing_distance[mid]:
                high = mid - 1
            elif pair_distance > ordered_circuits_increasing_distance[mid]:
                low = mid + 1
        index = low
        if pair_distance > ordered_circuits_increasing_distance[low]:
            index += 1
        ordered_circuits_increasing_distance.insert(index, pair_distance)
        ordered_circuits_locations.insert(index, [first, second])

print("List Sorted")

already_done = []
circuit_list = [[-1,-1]]


for location in ordered_circuits_locations:
    for circuit in circuit_list:
        first_circuit = -1
        second_circuit = -1
        for circuit_index, circuit in enumerate(circuit_list):
            if location[0] in circuit:
                first_circuit = circuit_index
            if location[1] in circuit:
                second_circuit = circuit_index
        if first_circuit == -1 and second_circuit == -1:
            circuit_list.append(location)
        elif first_circuit >= 0 and second_circuit >= 0:
            if first_circuit != second_circuit:
                for circuit_value in circuit_list[second_circuit]:
                    circuit_list[first_circuit].append(circuit_value)
                circuit_list.pop(second_circuit)
        elif first_circuit >= 0:
            circuit_list[first_circuit].append(location[1])
        elif second_circuit >= 0:
            circuit_list[second_circuit].append(location[0])
        already_done.append(copy.deepcopy(location))
    if len(circuit_list[1]) == len(input):
        print(box_coords[location[0]][0] * box_coords[location[1]][0])
        break