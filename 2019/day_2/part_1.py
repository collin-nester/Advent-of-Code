#Advent of Code Day 2 Part 1
import csv

def opcode_1():
    y = int(intcode[int(intcode[x])]) + int(intcode[int(intcode[x + 1])])
    intcode[int(intcode[x + 2])] = y

def opcode_2():
    y = int(intcode[int(intcode[x])]) * int(intcode[int(intcode[x + 1])])
    intcode[int(intcode[x + 2])] = y

with open('input.txt', 'r') as reader:
    intcode = reader.readlines()
    
    intcode = intcode[0].split(",")

    intcode[1] = 12
    intcode[2] = 2
    x = 1

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
    print(intcode)