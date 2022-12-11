import sys
from utils import *
with open("2022/day_10/input.txt", "r") as reader:
    program_list = reader.readlines()

register_x = 1
strength_total = 0
def add_to_total(x_value, cycle_number):
    global strength_total
    signal_strength = x_value * cycle_number
    strength_total += signal_strength

cycle = 0
signal_strength = 1
for i in program_list:
    cycle += 1
    if cycle % 40 == 20 and cycle <= 220:
        add_to_total(signal_strength, cycle)
    if i == "noop":
        continue
    if i[0:4] == "addx":
        cycle += 1
        if cycle % 40 == 20 and cycle <= 220:
            add_to_total(signal_strength, cycle)
        signal_strength += int(first_int(i))

print(strength_total)