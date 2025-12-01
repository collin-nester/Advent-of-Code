with open("2025/day1/input.txt", "r") as reader:
    input = reader.readlines()

current = 50
count = 0

for i in input:
    dir = i[0]
    size = int(i[1:])
    for j in range(size):
        current = (current + ((dir == "R") - (dir == "L"))) % 100
        count += (current == 0)
    print(current)

print(count)