#Advent of Code day 3 part 2

with open('/Users/collinnester24/Documents/python/GitHub/advent_of_code/2021/day_3/input.txt', 'r') as reader:
    diagnostic_report = reader.readlines()

most_common = []
matching_list = []
            
def figure_out_most_common_for_index_and_append():
    r = 0
    if len(matching_list) != 0:
        for k, l in enumerate(matching_list):
            if l[i] == str(1):
                r += 1
            elif l[i] == str(0):
               r -= 1
    else:
        for k, l in enumerate(diagnostic_report):
            if l[i] == str(1):
                r += 1
            elif l[i] == str(0):
               r -= 1
    if r >= 0:
        most_common.append("1")
    elif r < 0:
        most_common.append("0")

def put_matching_into_list():
    for j in diagnostic_report:
        if j[0:i] == most_common:
            matching_list.append(j)

for i in range(len(diagnostic_report[0].strip())):
    figure_out_most_common_for_index_and_append()
    matching_list.clear()
    most_common = "".join(most_common)
    put_matching_into_list()
    most_common = list(most_common)
print("".join(most_common))



least_common = []
matching_list = []

def figure_out_least_common_for_index_and_append():
    r = 0
    if len(matching_list) != 0:
        for k, l in enumerate(matching_list):
            if l[i] == str(1):
                r += 1
            elif l[i] == str(0):
                r -= 1
    else:
        for k, l in enumerate(diagnostic_report):
            if l[i] == str(1):
                r += 1
            elif l[i] == str(0):
                r -= 1
    if r >= 0:
        least_common.append("0")
    elif r < 0:
        least_common.append("1")

def put_matching_into_list():
    for j in diagnostic_report:
        if j[0:i] == least_common:
            matching_list.append(j)

def when_one_left_print():
    if len(matching_list) == 1:
        print(matching_list)

for i in range(len(diagnostic_report[0].strip())):
    figure_out_least_common_for_index_and_append()
    matching_list.clear()
    least_common = "".join(least_common)
    put_matching_into_list()
    least_common = list(least_common)
    when_one_left_print()
print("".join(least_common))