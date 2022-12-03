priority_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
priority_sum = 0

with open("2022/day_3/input.txt", "r") as reader:
    rucksack_contents_list = reader.readlines()

for i in rucksack_contents_list:
    if rucksack_contents_list.index(i) % 3 == 0:
        rucksack_one = i
        rucksack_two = rucksack_contents_list[int(rucksack_contents_list.index(i) + 1)]
        rucksack_three = rucksack_contents_list[int(rucksack_contents_list.index(i) + 2)]
        for j in rucksack_one:
            if j in rucksack_two and j in rucksack_three:
                priority_sum = priority_sum + priority_list.index(j) + 1
                break

print(priority_sum)