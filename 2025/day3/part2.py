with open("2025/day3/input.txt", "r") as reader:
    input = reader.readlines()

def find_largest(batteries, size_remaining):
    print(batteries + " " + str(size_remaining))
    largest = 0
    index_largest = 0
    if size_remaining == 0:
        return ""
    if len(batteries) == size_remaining:
        return batteries
    for n, battery in enumerate(batteries):
        if int(battery) > largest and len(batteries)-n >= size_remaining:
            largest = int(battery)
            index_largest = n
    return str(largest) + find_largest(batteries[index_largest+1:], size_remaining-1)

total_joltage = 0
for bank in input:
    batteries = bank.strip()
    batteries = str(batteries)
    largest = 0
    index_largest = 0
    largest = find_largest(batteries, 12)
    print(largest)
    total_joltage += int(largest)
    
print(total_joltage)