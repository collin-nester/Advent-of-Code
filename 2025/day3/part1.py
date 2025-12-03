with open("2025/day3/input.txt", "r") as reader:
    input = reader.readlines()

total_joltage = 0
for bank in input:
    batteries = bank.strip()
    batteries = str(batteries)
    largest = 0
    index_largest = 0
    for n, battery in enumerate(batteries):
        if int(battery) > largest and n+1 != len(batteries):
            largest = int(battery)
            index_largest = n
    second_largest = 0
    for part_battery in batteries[index_largest+1:]:
        if int(part_battery) > second_largest:
            second_largest = int(part_battery)
    total_joltage += int(str(largest) + str(second_largest))
    print(str(largest) + str(second_largest))
print(total_joltage)