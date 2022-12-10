import numpy as np

with open("2022/day_9/input.txt", "r") as reader:
    movement_list = reader.readlines()

movement_array = []
for i in movement_list:
    movement_array.append(i.split(" "))


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

# def move_tail(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos):
#     if head_x_pos == tail_x_pos:
#         if head_y_pos + 2 == tail_y_pos:
#             tail_y_pos += 1
#         elif head_y_pos - 2 == tail_y_pos:
#             tail_y_pos -= 1
#         return tail_x_pos, tail_y_pos
#     elif head_y_pos == tail_y_pos:
#         if head_x_pos + 2 == tail_x_pos:
#             tail_x_pos += 1
#         elif head_x_pos - 2 == tail_x_pos:
#             tail_x_pos -= 1
#         return tail_x_pos, tail_y_pos
#     elif head_x_pos + 1 == tail_y_pos or head_x_pos - 1 == tail_y_pos:


tail_x_pos = 5
tail_y_pos = 275
head_x_pos = 5
head_y_pos = 275
old_head_x_pos = 5
old_head_y_pos = 275
for i in movement_array:
    for j in range(int(i[1])):
        visited_matrix[tail_x_pos, tail_y_pos] = -1
        head_x_pos, head_y_pos = move_head(i, head_x_pos, head_y_pos)
        if (head_x_pos != tail_x_pos and head_x_pos + 1 != tail_x_pos and head_x_pos - 1 != tail_x_pos) or (head_y_pos != tail_y_pos and head_y_pos + 1 != tail_y_pos and head_y_pos - 1!= tail_y_pos):
            tail_x_pos = old_head_x_pos
            tail_y_pos = old_head_y_pos
        old_head_x_pos = int(head_x_pos)
        old_head_y_pos = int(head_y_pos)

visited_number = 0
for m, i in enumerate(visited_matrix):
    for j in i:
        if j == -1:
            visited_number += 1
print(visited_number)