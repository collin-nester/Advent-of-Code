current_calories = 0
calories_per_elf_list = []
current_max = 0
current_second = 0
current_third = 0

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
        current_third = current_second
        current_second = current_max
        current_max = i
    elif i > current_second:
        current_third = current_second
        current_second = i
    elif i > current_third:
        current_third = i
    

print(current_max)
print(current_second)
print(current_third)
print(current_third + current_max + current_second)