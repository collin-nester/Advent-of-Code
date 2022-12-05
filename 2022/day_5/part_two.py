readable_crate_list = []
movement_list = []
readable_movement_list = []
x = 0

with open("2022/day_5/input.txt", "r") as reader:
    crate_and_movement_list = reader.readlines()

for i in crate_and_movement_list:
    crate_and_movement_list[crate_and_movement_list.index(i)] = i.replace("\n", "")

crate_list = crate_and_movement_list[:9]
movement_list = crate_and_movement_list[10:]

for i in crate_list:
    readable_crate_list.append([])
for i in crate_list:
    y = 0
    for j in i:
        if (y % 4 == 1):
            readable_crate_list[int(y/4)].append(j)
        y = y + 1
    x = x + 1
for i in readable_crate_list:
    i.pop(-1)
    i = i.reverse()
for i in readable_crate_list:
    while " " in i:
        i.remove(" ")

for i in movement_list:
    readable_movement_list.append([])
    first = i.split(" from ")[0].replace("move ", "")
    second = i.split(" from ")[1].split(" to ")[0]
    third = i.split(" from ")[1].split(" to ")[1]
    readable_movement_list[-1].append(int(first))
    readable_movement_list[-1].append(int(second))
    readable_movement_list[-1].append(int(third))

for i in readable_movement_list:
    number_moved = i[0]
    starting_stack = i[1] - 1
    ending_stack = i[2] - 1
    currently_moving = readable_crate_list[starting_stack][-number_moved:]
    for k in currently_moving:
        readable_crate_list[ending_stack].append(k)
    for j in range(number_moved):
        readable_crate_list[starting_stack].pop(-1)

final_string = ""
for i in readable_crate_list:
    final_string = final_string + i[-1]
print(readable_crate_list)
print(final_string)