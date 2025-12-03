import math
with open("2025/day2/input.txt", "r") as reader:
    input = reader.readline()

input = input.split(",")
processed_input = []
for n, input in enumerate(input):
    processed_input.append(input.split("-"))

total = 0

for r in processed_input:
    start = int(r[0])
    end = int(r[1])
    for i in range(start,end+1):
        j = str(i)
        group = ""
        is_invalid = False
        for group_length in range(1,len(j)):
            if len(j) % group_length == 0:
                group = j[0:group_length]
                num_groups = int(len(j)/group_length)
                could_be_invalid = True
                for k in range(num_groups):
                    if j[k*group_length:group_length*(k+1)] != group:
                        could_be_invalid = False
                if could_be_invalid:
                    is_invalid = True
        total += is_invalid * i


print(total)