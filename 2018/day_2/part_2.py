one_removed_list = []
matching_list = []

with open ("2018\day_2\input.txt", "r") as reader:
    box_id_list = reader.readlines()


for i in box_id_list:
    for j in range(len(box_id_list[0])):
        new_string = i[:j]+i[j+1:]
        if new_string in one_removed_list:
            matching_list.append(new_string)
        one_removed_list.append(new_string)


print(len(one_removed_list))
print(matching_list)