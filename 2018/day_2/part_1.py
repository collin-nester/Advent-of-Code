number_of_ids_with_duplicates = 0
number_of_ids_with_triplicates = 0

with open ("2018\day_2\input.txt", "r") as reader:
    box_id_list = reader.readlines()


for i in box_id_list:
    for j in i:
        if i.count(j) == 2:
            number_of_ids_with_duplicates = number_of_ids_with_duplicates + 1
            break
    for j in i:
        if i.count(j) == 3:
            number_of_ids_with_triplicates = number_of_ids_with_triplicates + 1
            break

checksum = number_of_ids_with_duplicates * number_of_ids_with_triplicates

print(checksum)