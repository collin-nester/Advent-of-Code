import sys
from utils import *
import math

with open("2022\day_11\input.txt", "r") as reader:
    monkey_input_list = reader.read()

class monkey:
    def __init__(self, number, items, operation, operation_number, test_number, next_monkey_if_true, next_monkey_if_false) -> None:
        self.number = number
        self.items = items
        self.operation = operation
        self.operation_number = operation_number
        self.test_number = int(test_number)
        self.next_monkey_if_true = next_monkey_if_true
        self.next_monkey_if_false = next_monkey_if_false
        self.inspected_items = 0


    def inspect(self):
        self.inspected_items += len(self.items)
        for i in list(self.items):
            i = int(i)
            if self.operation == "*":
                if self.operation_number == "old":
                    i *= i
                else:
                    i *= int(self.operation_number)
            elif self.operation == "+":
                if self.operation_number == "old":
                    i += i
                else:
                    i += int(self.operation_number)
            if i % self.test_number == 0:
                monkey_list[self.next_monkey_if_true].items.append(i % loop_number)
                self.items.remove(self.items[0])
            else:
                monkey_list[self.next_monkey_if_false].items.append(i % loop_number)
                self.items.remove(self.items[0])

divisor_list = []
monkey_input_list = monkey_input_list.split("\n\n")
monkey_list = []
for n, i in enumerate(monkey_input_list):
    monkey_input_list[n] = i.split("\n")

for n, i in enumerate(monkey_input_list):
    monkey_number = first_int(i[0])
    starting_items = ints(i[1])
    operation = i[2][23]
    operation_number = i[2][25:]
    test_number = first_int(i[3])
    divisor_list.append(test_number)
    next_monkey_if_true = first_int(i[4])
    next_monkey_if_false = first_int(i[5])
    monkey_list.append(monkey(monkey_number, starting_items, operation, operation_number, test_number, next_monkey_if_true, next_monkey_if_false))

loop_number = 1
for i in divisor_list:
    loop_number *= i

for i in range(10000):
    for j in monkey_list:
        j.inspect()

max_inspected = 0
second_most_inspected = 0
for i in monkey_list:
    print(i.inspected_items)
    if i.inspected_items > max_inspected:
        second_most_inspected = max_inspected
        max_inspected = i.inspected_items
    elif i.inspected_items > second_most_inspected:
        second_most_inspected = i.inspected_items
print(max_inspected)
print(second_most_inspected)
print(max_inspected * second_most_inspected)