#Advent of Code day 3 part 1

with open('/Users/collinnester24/Documents/python/GitHub/advent_of_code/2021/day_3/input.txt', 'r') as reader:
    diagnostic_report = reader.readlines()

gamma_rate = 0
epsilon_rate = 0
common_list = []
for i in range(len(diagnostic_report[0])-1):
    common_list.append(0)

for j in diagnostic_report:
    j.strip()
    for k, l in enumerate(j):
        if l == str(1):
            common_list[k] += 1
        elif l == str(0):
            common_list[k] -= 1

for i, j in enumerate(common_list):
    if j > 0:
        common_list[i] = str(1)
    else:
        common_list[i] = str(0)
common_list = "".join(common_list)
print(int(common_list))