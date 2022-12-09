import numpy as np

with open("2022/day_8/input.txt", "r") as reader:
    tree_list = reader.readlines()

tree_array = np.zeros((len(tree_list), len(tree_list[0]) - 1))
viewing_distance_array = []

for i, n in enumerate(tree_list):
    n = n.strip()
    for j, m in enumerate(n):
        tree_array[i][j] = int(m)

def scan_left(row_number, column_number, row_data, tree_data):
    x = tree_data
    visible_distance = 0
    for i in range(column_number, 0, -1):
        visible_distance += 1
        if row_data[i - 1] >= x:
            break
    return visible_distance

def scan_right(row_number, column_number, row_data, tree_data):
    x = tree_data
    visible_distance = 0
    for i in range(column_number + 1, len(row_data), 1):
        visible_distance += 1
        if row_data[i] >= x:
            break
    return visible_distance

def scan_down(row_number, column_number, row_data, tree_data):
    x = tree_data
    visible_distance = 0
    for i in range(row_number + 1, len(tree_array), 1):
        visible_distance += 1
        if tree_array[i][column_number] >= x:
            break
    return visible_distance

def scan_up(row_number, column_number, row_data, tree_data):
    x = tree_data
    visible_distance = 0
    for i in range(row_number, 0, -1):
        visible_distance += 1
        if tree_array[i - 1][column_number] >= x:
            break
    return visible_distance

def scan_for_view_distance():
    for m, i in enumerate(tree_array):
        for n, j in enumerate(i):
            left = scan_left(m, n, i, j)
            right = scan_right(m, n, i, j)
            up = scan_up(m, n, i, j)
            down = scan_down(m, n, i, j)
            viewing_distance = [left, right, up, down]
            viewing_distance_array.append(viewing_distance)

def calculate_scenic_score():
    max_scenic_score = 0
    for i in viewing_distance_array:
        scenic_score = i[0] * i[1] * i[2] * i[3]
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score
    return max_scenic_score
    

def main():
    scan_for_view_distance()
    print(calculate_scenic_score())

main()