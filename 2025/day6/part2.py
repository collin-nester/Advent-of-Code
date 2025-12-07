with open("2025/day6/input.txt", "r") as reader:
    input = reader.readlines()

processed_input = []
for row in input:
    processed_row = row.split(" ")
    indices_to_delete = []
    for index, entry in enumerate(processed_row):
        processed_row[index] = entry.strip()
        if processed_row[index] == '':
            indices_to_delete.append(index)
    for index in range(len(indices_to_delete)):
        processed_row.pop(indices_to_delete[len(indices_to_delete)-1-index])
    processed_input.append(processed_row)

space_column_indices = [-1]
for column in range(len(input[0])-1):
    is_space_column = True
    for row in range(len(input)):
        if input[row][column] != ' ':
            is_space_column = False
    if is_space_column:
        space_column_indices.append(column)
space_column_indices.append(len(input[0])-1)

total = 0
num_list = []
for column in range(len(input[0])):
    if column in space_column_indices:
        symbol_column = space_column_indices[space_column_indices.index(column)-1]+1
        print(symbol_column)
        is_multiplication = (input[len(input)-1][symbol_column] == "*")
        is_addition = not is_multiplication
        value = int(is_multiplication)
        for num in num_list:
            if is_multiplication:
                value *= num
            if is_addition:
                value += num
        total += value
        num_list = []
    else:
        num_to_add = ""
        for i in range(len(input)-1):
            num_to_add += input[i][column]
        num_to_add = int(num_to_add.strip())
        num_list.append(num_to_add)


""" for column in range(len(processed_input[0])):
    is_multiplication = (processed_input[-1][column] == "*")
    is_addition = not is_multiplication
    column_value = int(is_multiplication)
    for row in range(len(processed_input)-1):
        if is_multiplication:
            column_value *= int(processed_input[row][column])
        if is_addition:
            column_value += int(processed_input[row][column])
    total += column_value """

print(total)