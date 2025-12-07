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

total = 0
for column in range(len(processed_input[0])):
    is_multiplication = (processed_input[-1][column] == "*")
    is_addition = not is_multiplication
    column_value = int(is_multiplication)
    for row in range(len(processed_input)-1):
        if is_multiplication:
            column_value *= int(processed_input[row][column])
        if is_addition:
            column_value += int(processed_input[row][column])
    total += column_value

print(total)