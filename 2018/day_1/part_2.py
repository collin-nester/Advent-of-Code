total_frequency = 0
total_frequencies_list = [0]
x = 0

with open ("2018\day_1\input.txt", "r") as reader:
    input = reader.readlines()

while x != 1:
    for i in input:
        new_frequency = int(i)
        total_frequency = total_frequency + new_frequency
        if total_frequency in total_frequencies_list:
            print(total_frequency)
            x = 1
            break
        total_frequencies_list.append(total_frequency)
            

print(total_frequency)