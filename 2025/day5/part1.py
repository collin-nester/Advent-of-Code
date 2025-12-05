with open("2025/day5/input.txt", "r") as reader:
    input = reader.readlines()

def is_in_range(start_range, end_range, num):
    return num >= start_range and num <= end_range

blank_line = -1
for n, r in enumerate(input):
    if r == "\n":
        blank_line = n
    input[n] = input[n].strip()

ranges = input[:blank_line]
ingredients = input[blank_line+1:]
num_in_range = 0

for ing in ingredients:
    in_range = False
    for range in ranges:
        start_range = int(range.split("-")[0])
        end_range = int(range.split("-")[1])
        if is_in_range(start_range, end_range, int(ing)):
            in_range = True
            break
    if in_range:
        num_in_range += 1
print(num_in_range)