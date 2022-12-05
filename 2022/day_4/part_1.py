fully_contained = 0

with open("2022/day_4/input.txt", "r") as reader:
    cleanup_list = reader.readlines()

for i in cleanup_list:
    pre_split_list = i.split("-")
    elf_one_start = int(pre_split_list[0])
    elf_one_finish = int(pre_split_list[1].split(",")[0])
    elf_two_start = int(pre_split_list[1].split(",")[1])
    elf_two_finish = int(pre_split_list[2])
    if (elf_two_finish >= elf_one_finish and elf_two_start <= elf_one_start) or (elf_two_finish <= elf_one_finish and elf_two_start >= elf_one_start):
        fully_contained = fully_contained + 1

print(fully_contained)