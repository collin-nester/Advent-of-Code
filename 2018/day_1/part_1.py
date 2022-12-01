total_frequency = 0

with open ("2018\day_1\input.txt", "r") as reader:
    input = reader.readlines()

for i in input:
    new_frequency = int(i)
    total_frequency = total_frequency + new_frequency

print(total_frequency)