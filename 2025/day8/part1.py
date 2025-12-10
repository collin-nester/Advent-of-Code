import copy
import numpy as np

with open("2025/day8/input.txt", "r") as reader:
    input = reader.readlines()

PAIRS_TO_CONNECT = 1000

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
    if first % 1 == 0:
        print("Ordered " + str(first) + " Potential Connections")
    for second, box_coords2 in enumerate(box_coords[first+1:]):
        second += first + 1
        if distance_between[first][second] < ordered_circuits_increasing_distance[-1] or len(ordered_circuits_increasing_distance) <= PAIRS_TO_CONNECT:
            for index, distance in enumerate(ordered_circuits_increasing_distance):
                if distance_between[first][second] < distance:
                    ordered_circuits_increasing_distance.insert(index, distance_between[first][second])
                    ordered_circuits_locations.insert(index, [first, second])
                    break
            if len(ordered_circuits_increasing_distance) > PAIRS_TO_CONNECT:
                ordered_circuits_increasing_distance.pop()
                ordered_circuits_locations.pop()

print("List Sorted")

already_done = []
circuit_list = [[-1,-1]]

for location in ordered_circuits_locations[:PAIRS_TO_CONNECT]:
    print("Connected " + str(ordered_circuits_locations.index(location)) + " Boxes")
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

print(circuit_list)

product = 1
for i in range(3):
    max_length = 0
    index = -1
    for j in circuit_list:
        if max_length < len(j):
            max_length = len(j)
            index = circuit_list.index(j)
    product *= max_length
    circuit_list.pop(index)

print(product)