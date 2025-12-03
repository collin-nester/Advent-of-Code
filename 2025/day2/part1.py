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
        i = str(i)
        if len(i) % 2 == 0 and i[:int(len(i)/2)] == i[int(len(i)/2):]:
            total += int(i)

print(total)