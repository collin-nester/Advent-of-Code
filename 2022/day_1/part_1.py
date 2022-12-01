current_calories = 0
calories_per_elf_list = []
current_max = 0

with open ("2022\day_1\input.txt", "r") as reader:
    calorie_list = reader.readlines()

for i in calorie_list:
    if i == "\n":
        calories_per_elf_list.append(int(current_calories))
        current_calories = 0
    else:
        current_calories = current_calories + int(i.replace("\n",""))

for i in calories_per_elf_list:
    if i > current_max:
        current_max = i

print(current_max)