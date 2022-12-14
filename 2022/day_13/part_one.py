import sys
from utils import *

with open("2022/day_13/input.txt", "r") as reader:
    input = reader.read()

parsed_input = input.split("\n\n")
for n, i in enumerate(parsed_input):
    parsed_input[n] = i.split("\n")

lists_list = list()
for i in parsed_input:
    lists_list.append(list())
    for j in i:
        bracket_counter = 0
        for k in j:
            if k == "[":
                if bracket_counter == 0:
                    lists_list[-1].append(list())
                elif bracket_counter == 1:
                    lists_list[-1][-1].append(list())
                elif bracket_counter == 2:
                    lists_list[-1][-1][-1].append(list())
                elif bracket_counter == 3:
                    lists_list[-1][-1][-1][-1].append(list())
                elif bracket_counter == 4:
                    lists_list[-1][-1][-1][-1][-1].append(list())
                elif bracket_counter == 5:
                    lists_list[-1][-1][-1][-1][-1][-1].append(list())
                elif bracket_counter == 6:
                    lists_list[-1][-1][-1][-1][-1][-1][-1].append(list())
                elif bracket_counter == 7:
                    lists_list[-1][-1][-1][-1][-1][-1][-1][-1].append(list())
                elif bracket_counter == 8:
                    lists_list[-1][-1][-1][-1][-1][-1][-1][-1][-1].append(list())
                elif bracket_counter == 9:
                    lists_list[-1][-1][-1][-1][-1][-1][-1][-1][-1][-1].append(list())
                bracket_counter += 1
            elif k == "]":
                bracket_counter -= 1
            elif k == ",":
                pass
            else:
                k = int(k)
                if bracket_counter == 1:
                    lists_list[-1][-1].append(k)
                elif bracket_counter == 2:
                    lists_list[-1][-1][-1].append(k)
                elif bracket_counter == 3:
                    lists_list[-1][-1][-1][-1].append(k)
                elif bracket_counter == 4:
                    lists_list[-1][-1][-1][-1][-1].append(k)
                elif bracket_counter == 5:
                    lists_list[-1][-1][-1][-1][-1][-1].append(k)
                elif bracket_counter == 6:
                    lists_list[-1][-1][-1][-1][-1][-1][-1].append(k)
                elif bracket_counter == 7:
                    lists_list[-1][-1][-1][-1][-1][-1][-1][-1].append(k)
                elif bracket_counter == 8:
                    lists_list[-1][-1][-1][-1][-1][-1][-1][-1][-1].append(k)
                elif bracket_counter == 9:
                    lists_list[-1][-1][-1][-1][-1][-1][-1][-1][-1][-1].append(k)
                elif bracket_counter == 10:
                    lists_list[-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1].append(k)

def compare_ints(left_int, right_int):
    if left_int != right_int:
        if left_int < right_int:
            return True
        elif left_int > right_int:
            return False

def compare_list_of_ints(left_list, right_list):
    if len(left_list) <= len(right_list):
        for n, i in enumerate(left_list):
            if compare_ints(i, right_list[n]) == (True or False):
                return compare_ints(i, right_list[n])
        if len(left_list) != len(right_list):
            return True
    elif len(left_list) > len(right_list):
        for n, i in right_list:
            if compare_ints(left_list[n], i) == (True or False):
                return compare_ints(left_list[n], i)
        if len(left_list) != len(right_list):
            return False

def compare_lists(left_list, right_list):
    if (type(left_list) and type(right_list)) == int:
        if compare_ints(left_list, right_list) != None:
            return compare_ints(left_list, right_list)
    else:
        for n, i in enumerate(left_list):
            try:
                if (type(left_list) and type(right_list)) == int:
                    if compare_ints(left_list, right_list) != None:
                        return compare_ints(left_list, right_list)
                elif type(i) == int and type(right_list[n]) == int:
                    if compare_ints(i, right_list[n]) != None:
                        return compare_ints(i, right_list[n])
                elif type(i) != type(right_list[n]):
                    if type(i) == int:
                        i = [i]
                    elif type(right_list[n]) == int:
                        right_list[n] = [right_list[n]]
                    return compare_lists(i, right_list[n])
                elif list() not in (left_list or right_list) and compare_list_of_ints(i, right_list[n]) == (True or False):
                    return compare_list_of_ints(i, right_list[n])
                else:
                    return compare_lists(i, right_list[n])
            except:
                return False




correct_indices_sum = 0

for n, i in enumerate(lists_list):
    if compare_lists(i[0], i[1]) == True:
        correct_indices_sum += (n + 1)

print(correct_indices_sum)