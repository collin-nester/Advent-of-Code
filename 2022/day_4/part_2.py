partially_contained = 0

with open("2022/day_4/input.txt", "r") as reader:
    cleanup_list = reader.readlines()

for i in cleanup_list:
    pre_split_list = i.split("-")
    elf_one_start = int(pre_split_list[0])
    elf_one_finish = int(pre_split_list[1].split(",")[0])
    elf_two_start = int(pre_split_list[1].split(",")[1])
    elf_two_finish = int(pre_split_list[2])
    if (elf_one_start <= elf_two_start and elf_two_start <= elf_one_finish) or (elf_two_start <= elf_one_start and elf_one_start <= elf_two_finish):
        partially_contained = partially_contained + 1

print(partially_contained)