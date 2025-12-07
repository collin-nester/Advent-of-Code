import copy
import pprint
import numpy as np

with open("2025/day7/input.txt", "r") as reader:
    input = reader.readlines()

def return_modified_memo_matrix(input, cur_pos, memo_matrix):
    if cur_pos[0] == len(input) - 1:
        memo_matrix[cur_pos[0]][cur_pos[1]] = 1
        return memo_matrix
    next_pos = [cur_pos[0] + 1, cur_pos[1]]
    if memo_matrix[next_pos[0]][next_pos[1]] != 0:
        memo_matrix[cur_pos[0]][cur_pos[1]] = memo_matrix[next_pos[0]][next_pos[1]]
        return memo_matrix
    if input[next_pos[0]][next_pos[1]] == '^':
        next_pos[1] -= 1
        memo_matrix = return_modified_memo_matrix(input, next_pos, memo_matrix)
        next_pos[1] += 2
        memo_matrix = return_modified_memo_matrix(input, next_pos, memo_matrix)
        izquierda = memo_matrix[next_pos[0]][next_pos[1]-2]
        derecha = memo_matrix[next_pos[0]][next_pos[1]]
        memo_matrix[cur_pos[0]][cur_pos[1]] = izquierda + derecha
        return memo_matrix
    else:
        memo_matrix = return_modified_memo_matrix(input, next_pos, memo_matrix)
        memo_matrix[cur_pos[0]][cur_pos[1]] = memo_matrix[next_pos[0]][next_pos[1]]
        return memo_matrix

for index in range(len(input)):
    input[index] = input[index].strip()
start_col = -1
beam_array = []
for col in range(len(input[0])):
    if input[0][col] == "S":
        start_col = col
        beam_array.append("|")
    else:
        beam_array.append(".")

memo_matrix = np.zeros([len(input), len(input[0])])

memo_matrix = return_modified_memo_matrix(input, [0, start_col], memo_matrix)

timelines = memo_matrix[0][start_col]

print(timelines)

with open("2025/day7/output.txt", "w") as writer:
    for line in memo_matrix:
        print(line)
        print()
        writer.writelines(str(line))