with open("2025/day5/input.txt", "r") as reader:
    input = reader.readlines()

def is_in_range(start_range, end_range, num):
    return num >= start_range and num <= end_range

def combine_ranges(new_range, start_range, end_range):
    new_start_range = int(new_range.split("-")[0])
    new_end_range = int(new_range.split("-")[1])
    absorbed = False
    if is_in_range(new_start_range, new_end_range, start_range) and end_range > new_end_range:
        new_end_range = end_range
    if is_in_range(new_start_range, new_end_range, end_range) and start_range < new_start_range:
        new_start_range = start_range
    if is_in_range(new_start_range, new_end_range, start_range) or is_in_range(new_start_range, new_end_range, end_range):
        absorbed = True
    new_range = str(new_start_range) + "-" + str(new_end_range)
    return absorbed, new_range

blank_line = -1
for n, r in enumerate(input):
    if r == "\n":
        blank_line = n
    input[n] = input[n].strip()

ranges = input[:blank_line]
new_ranges = [input[0]]
old_ranges = []

for num_range in ranges:
    start_range = int(num_range.split("-")[0])
    end_range = int(num_range.split("-")[1])
    absorbed = False
    for index, new_range in enumerate(new_ranges):
        was_absorbed, new_range = combine_ranges(new_range, start_range, end_range)
        if was_absorbed:
            absorbed = True
            new_ranges[index] = new_range
            break
    if not absorbed:
        new_ranges.append(num_range)

while old_ranges != new_ranges:
    old_ranges = new_ranges
    indices_to_delete = []
    for n, num_range in enumerate(new_ranges):
        start_range = int(num_range.split("-")[0])
        end_range = int(num_range.split("-")[1])
        absorbed = False
        for index, new_range in enumerate(new_ranges):
            was_absorbed, new_range = combine_ranges(new_range, start_range, end_range)
            if was_absorbed and index > n:
                absorbed = True
                new_ranges[index] = new_range
                indices_to_delete.append(n)
                break
    for indices in range(len(indices_to_delete)):
        index = len(indices_to_delete) - indices - 1
        new_ranges.pop(indices_to_delete[index])

total = 0

for num_range in new_ranges:
    start_range = int(num_range.split("-")[0])
    end_range = int(num_range.split("-")[1])
    total += end_range - start_range + 1

print(total)