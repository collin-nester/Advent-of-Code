import numpy as np

with open("2022/day_8/input.txt", "r") as reader:
    tree_list = reader.readlines()

tree_array = np.zeros((len(tree_list), len(tree_list[0]) - 1))
seen_array = np.zeros((len(tree_list), len(tree_list[0]) - 1))

for i, n in enumerate(tree_list):
    n = n.strip()
    for j, m in enumerate(n):
        tree_array[i][j] = int(m)


def scan_from_left():
    for n, i in enumerate(tree_array):
        x = -1
        for m, j in enumerate(i):
            if j > x:
                x = j
                seen_array[n][m] = -1


def scan_from_right():
    rotated = np.fliplr(tree_array)
    for n, i in enumerate(rotated):
        x = -1
        for m, j in enumerate(i):
            if j > x:
                x = j
                seen_array[n][98-m] = -1

def scan_from_top():
    rotated = np.rot90(tree_array, -1, (0,1))
    rotated = np.fliplr(rotated)
    print(rotated)
    for n, i in enumerate(rotated):
        x = -1
        for m, j in enumerate(i):
            if j > x:
                x = j
                seen_array[m][n] = -1

def scan_from_bottom():
    rotated = np.rot90(tree_array, -1, (0,1))
    print(rotated)
    for n, i in enumerate(rotated):
        x = -1
        for m, j in enumerate(i):
            if j > x:
                x = j
                seen_array[98-m][n] = -1


def count_visible():
    number_seen = 0
    for i in seen_array:
        for j in i:
            if j == -1:
                number_seen += 1
    return number_seen

def main():
    scan_from_left()
    scan_from_right()
    scan_from_top()
    scan_from_bottom()
    print(count_visible())

main()
print(seen_array)