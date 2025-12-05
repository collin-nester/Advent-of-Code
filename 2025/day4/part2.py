with open("2025/day4/input.txt", "r") as reader:
    input = reader.readlines()

def number_around(grid, row, col):
    num = 0
    #up
    if row != 0 and grid[row-1][col] == "@":
        num += 1
    #down
    if row+1 != len(grid) and grid[row+1][col] == "@":
        num += 1
    #left
    if col != 0 and grid[row][col-1] == "@":
        num += 1
    #right
    if col+1 != len(grid[0]) and grid[row][col+1] == "@":
        num += 1
    #nw
    if row != 0 and col != 0 and grid[row-1][col-1] == "@":
        num += 1
    #ne
    if row != 0 and col+1 != len(grid[0]) and grid[row-1][col+1] == "@":
        num += 1
    #se
    if row+1 != len(grid) and col+1 != len(grid[0]) and grid[row+1][col+1] == "@":
        num += 1
    #sw
    if row+1 != len(grid) and col != 0 and grid[row+1][col-1] == "@":
        num += 1
    return num


accessible_rolls = 0
prev_accessible_rolls = -1

while accessible_rolls != prev_accessible_rolls:
    prev_accessible_rolls = accessible_rolls
    for row in range(len(input)):
        input[row] = input[row].strip()
        for col in range(len(input[0])):
            if input[row][col] == "@" and number_around(input,row,col) < 4:
                accessible_rolls += 1
                if col == 0:
                    input[row] = "." + input[row][1:]
                elif col == len(input[0]):
                    input[row] = input[row][:-2] + "."
                else:
                    input[row] = input[row][:col] + "." + input[row][col+1:]

print(accessible_rolls)