import sys
import numpy as np
from utils import *
with open("2022/day_10/input.txt", "r") as reader:
    program_list = reader.readlines()

screen = np.empty(240)

strength_total = 0

def add_pixel(pixel_number, cycle):
    if cycle % 40 == pixel_number % 40 or cycle % 40 == pixel_number + 1 or cycle % 40 == pixel_number + 2:
        screen[cycle - 1] = "0"
    else:
        screen[cycle - 1] = "1"

cycle = 0
signal_strength = 1
for i in program_list:
    cycle += 1
    add_pixel(signal_strength, cycle)
    if i[0:4] == "addx":
        cycle += 1
        add_pixel(signal_strength, cycle)
        signal_strength += int(first_int(i))

screen = screen.reshape((6, 40))
horizontal_strip = ""
for i in screen:
        for j in i:
            if j == 0:
                horizontal_strip += '■'
            if j == 1:
                horizontal_strip += ' '
        print(horizontal_strip)
        horizontal_strip = ""