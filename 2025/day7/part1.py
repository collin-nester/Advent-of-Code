import copy
import pprint

with open("2025/day7/input.txt", "r") as reader:
    input = reader.readlines()

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

beam_matrix = copy.deepcopy(beam_array)
total_splits = 0
for row_index, row in enumerate(input[1:]):
    for col_index, col in enumerate(row):
        if col == '^' and beam_array[col_index] == '|':
            total_splits += 1
            beam_array[col_index-1] = '|'
            beam_array[col_index+1] = '|'
            beam_array[col_index] = '^'
        elif col == '.' and beam_array[col_index] == '^':
            beam_array[col_index] = '.'
        elif col == '.' and beam_array[col_index] == '|':
            beam_array[col_index] = '|'
    beam_matrix.append(copy.deepcopy(beam_array))
pprint.pprint(beam_matrix)
print(total_splits)