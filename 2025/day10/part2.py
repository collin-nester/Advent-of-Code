import numpy as np
from sympy import Matrix
import pprint
import copy

with open ("2025/day10/input.txt", "r") as reader:
    input = reader.readlines()

def process_line(line):
    split_line = line.split(" ")
    buttons = []
    for button in split_line[1:-1]:
        button_nums = []
        for num in button[1:-1].split(","):
            button_nums.append(int(num))
        buttons.append(button_nums)
    joltages = []
    for joltage in split_line[-1].strip()[1:-1].split(","):
        joltages.append(int(joltage))
    return buttons, joltages

def solves_lights(lights_buttons, button_presses, joltages):
    mult = np.matmul(lights_buttons,button_presses)
    for n, j in enumerate(joltages):
        if abs(mult[n]-j) <= 0.01:
            return False
    return True

total = 0
for line in input:
    buttons, joltages = process_line(line)
    lights_buttons = np.zeros((len(joltages), len(buttons)+1))
    for light in range(len(joltages)):
        for button_index in range(len(buttons)):
            if light in buttons[button_index]:
                lights_buttons[light][button_index] = 1
    for index, jolt in enumerate(joltages):
        lights_buttons[index][-1] = jolt
        
    rref, pivot_cols = Matrix(lights_buttons).rref()
    rref = np.array(rref)
    solution_row = np.zeros(len(rref))
    for num in range(len(rref)):
        solution_row[num] = rref[num][-1]
    while len(solution_row) < len(lights_buttons[0]):
        solution_row = np.append(solution_row, np.zeros(1))

    # # check if it's fully reduced
    # if len(pivot_cols) == len(rref[0])-1:
    #     total += sum(solution_row[:len(lights_buttons[0])])

    maximum_button_presses = max(solution_row)
    pivot_cols = set(pivot_cols)
    non_pivots_set = set((0,1,2,3,4,5,6,7,8,9)[:len(rref[0])-1])
    non_pivots_set = non_pivots_set.difference(pivot_cols)
    non_pivots = []
    for non_pivot in non_pivots_set:
        non_pivots.append(non_pivot)
    
    if len(pivot_cols) == len(rref[0])-1:
        total += sum(solution_row[:len(lights_buttons[0])])

    elif len(non_pivots) == 1:
        minimum = 0
        for i in range(round(maximum_button_presses)):
            temp_guess_solution = np.zeros(len(rref[0]))
            temp_guess_solution[int(non_pivots[0])] = i
            temp_results = np.matmul(rref, temp_guess_solution)
            new_solution_row = copy.deepcopy(solution_row)
            for index, result in enumerate(temp_results):
                solution_row[index] -= result
            print(i)
            print(solution_row)
            print(rref)
            print(solves_lights(lights_buttons, solution_row, joltages))

        #total += minumum


    elif len(non_pivots) == 2:
        continue
    
    elif len(non_pivots) == 3:
        continue


print(total)