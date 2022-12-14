import sys
from utils import *
import numpy as np
import math

with open ("2022/day_12/input.txt", "r") as reader:
    input = reader.read()

class node():
    def __init__(self, node_value, node_smallest_distance) -> None:
        self.node_value = node_value
        self.node_smallest_distance = node_smallest_distance

alpha_set = alpha_set()

def can_climb(starting_letter, ending_letter):
    if alpha_set.index(starting_letter) + 1 >= alpha_set.index(ending_letter):
        return True
    else:
        return False

def return_new_length(old_length, from_node_length, starting_letter, ending_letter):
    if old_length > from_node_length + 1 and can_climb(starting_letter, ending_letter):
        return from_node_length + 1
    else:
        return old_length

def check_adjacent_nodes(curr_node, curr_pos):
    try: #up
        topo_map[curr_pos[0] - 1][curr_pos[1]].node_smallest_distance = return_new_length(topo_map[curr_pos[0] - 1][curr_pos[1]].node_smallest_distance, curr_node.node_smallest_distance, curr_node.node_value, topo_map[curr_pos[0] - 1][curr_pos[1]].node_value)
    except:
        pass
    try: #down
        topo_map[curr_pos[0] + 1][curr_pos[1]].node_smallest_distance = return_new_length(topo_map[curr_pos[0] + 1][curr_pos[1]].node_smallest_distance, curr_node.node_smallest_distance, curr_node.node_value, topo_map[curr_pos[0] + 1][curr_pos[1]].node_value)
    except:
        pass
    try: #right
        topo_map[curr_pos[0]][curr_pos[1] - 1].node_smallest_distance = return_new_length(topo_map[curr_pos[0]][curr_pos[1] - 1].node_smallest_distance, curr_node.node_smallest_distance, curr_node.node_value, topo_map[curr_pos[0]][curr_pos[1] - 1].node_value)
    except:
        pass
    try: #left  
        topo_map[curr_pos[0]][curr_pos[1] + 1].node_smallest_distance = return_new_length(topo_map[curr_pos[0]][curr_pos[1] + 1].node_smallest_distance, curr_node.node_smallest_distance, curr_node.node_value, topo_map[curr_pos[0]][curr_pos[1] + 1].node_value)        
    except:
        pass

z = 0
def main():
    global topo_map, z
    topo_map = np.ndarray(0)
    x = 0
    y = 0
    my_z = -1
    final_node_position = []
    for i in input: 
        if i != "\n":
            if x % 64 == 0:
                y += 1
                my_z += 1
            if i == "b" and z == my_z:
                new_node = node("b", 1)
            elif i == "E":
                final_node_position = (x % 64, y - 1)
                new_node = node("z", math.inf)
            else:
                new_node = node(i, math.inf)
            topo_map = np.append(topo_map, new_node)
            x += 1
    topo_map = np.reshape(topo_map, (41, 64))


    for i in range(500):
        for n, j in enumerate(topo_map):
            for m, k in enumerate(j):
                check_adjacent_nodes(k, (n, m))

    return topo_map[final_node_position[1]][final_node_position[0]].node_smallest_distance


distance_list = list()
for i in range(41):
    distance_list.append(main())
    z += 1
print(min(distance_list))