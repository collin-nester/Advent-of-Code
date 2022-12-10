import numpy as np

with open("2022/day_9/input.txt", "r") as reader:
    movement_list = reader.readlines()

movement_array = []
for i in movement_list:
    movement_array.append(i.split(" "))

rope_list = []
for i in range(10):
    rope_list.append([5, 275])

visited_matrix = np.zeros(300 * 300)
visited_matrix = visited_matrix.reshape((300, 300))

def move_head(movement, x_pos, y_pos):
    if movement[0] == "R":
        x_pos += 1
    if movement[0] == "L":
        x_pos -= 1
    if movement[0] == "U":
        y_pos += 1
    if movement[0] == "D":
        y_pos -= 1
    return x_pos, y_pos

def not_in_range(head_x_pos, tail_x_pos, head_y_pos, tail_y_pos):
    if (head_x_pos != tail_x_pos and head_x_pos + 1 != tail_x_pos and head_x_pos - 1 != tail_x_pos) or (head_y_pos != tail_y_pos and head_y_pos + 1 != tail_y_pos and head_y_pos - 1!= tail_y_pos):
        return True

def move_tail(i, head, tail, n):
    if n == 0:
        head[0], head[1] = move_head(i, head[0], head[1])
    if not_in_range(head[0], tail[0], head[1], tail[1]) and n != 9:
        if head[0] == tail[0] and head[1] > tail[1]:
            tail[1] += 1
        elif head[0] == tail[0] and head[1] < tail[1]:
            tail[1] -= 1
        elif head[0] > tail[0] and head[1] == tail[1]:
            tail[0] += 1
        elif head[0] < tail[0] and head[1] == tail[1]:
            tail[0] -= 1
        elif head[0] > tail[0] and head[1] > tail[1]:
            tail[0] += 1
            tail[1] += 1
        elif head[0] > tail[0] and head[1] < tail[1]:
            tail[0] += 1
            tail[1] -= 1
        elif head[0] < tail[0] and head[1] < tail[1]:
            tail[0] -= 1
            tail[1] -= 1
        elif head[0] < tail[0] and head[1] > tail[1]:
            tail[0] -= 1
            tail[1] += 1
    return head, tail


def move():
    for i in movement_array:
        for j in range(int(i[1])):
            for n, k in enumerate(rope_list):
                if n == 9:
                    visited_matrix[k[0], k[1]] = -1
                rope_list[n], rope_list[n-9]= move_tail(i, k, rope_list[n-9], n)
            
def count_visited_matrix():
    visited_number = 0
    for m, i in enumerate(visited_matrix):
        for j in i:
            if j == -1:
                visited_number += 1
    return visited_number

move()
print(count_visited_matrix())