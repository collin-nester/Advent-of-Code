#Advent of Code Day 2 Part 2
import csv

def opcode_1():
    y = int(intcode[int(intcode[x])]) + int(intcode[int(intcode[x + 1])])
    intcode[int(intcode[x + 2])] = y

def opcode_2():
    y = int(intcode[int(intcode[x])]) * int(intcode[int(intcode[x + 1])])
    intcode[int(intcode[x + 2])] = y

with open('Advent-of-Code/2019/Day 2/input.txt', 'r') as reader:
    original_intcode = reader.readlines()
for y in range(0,100):
    for z in range(0,100):

        intcode = original_intcode[0].split(",")
        x = 1

        intcode[1] = y
        intcode[2] = z

        for i in intcode:
            if x % 4 - 1 == 0:
                if int(i) == 1:
                    opcode_1()
                elif int(i) == 2:
                    opcode_2()
                elif int(i) == 99:
                    break
                else:
                    print("Your code sucks " + str(i))
            x = x + 1
        if intcode[0] == 19690720:
            print(100 * y + z)
            print(y)
            print(z)