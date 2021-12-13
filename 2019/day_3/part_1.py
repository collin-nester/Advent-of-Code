#Advent of Code Day 3 Part 1
with open('input.txt', 'r') as reader:
    input = reader.readlines()
    line1 = input[0].split(",")
    line2 = input[1].split(",")
    line1[-1] = line1[-1][0:-1]
    line2[-1] = line2[-1][0:-1]
    line1_points = []
    line2_points = []
    x = 0
    y = 0
    for j in line1:
        if j[0] == "U":
            n = int(j[1:])
            for i in range(n):
                x = x + 1
                point = [x, y]
                line1_points.append(point)
        elif j[0] == "D":
            n = int(j[1:])
            for i in range(n):
                x = x - 1
                point = [x, y]
                line1_points.append(point)
        elif j[0] == "R":
            n = int(j[1:])
            for i in range(n):
                y = y + 1
                point = [x, y]
                line1_points.append(point)
        if j[0] == "L":
            n = int(j[1:])
            for i in range(n):
                y = y - 1
                point = [x, y]
                line1_points.append(point)
    for j in line2:
        if j[0] == "U":
            n = int(j[1:])
            for i in range(n):
                x = x + 1
                point = [x, y]
                line2_points.append(point)
        elif j[0] == "D":
            n = int(j[1:])
            for i in range(n):
                x = x - 1
                point = [x, y]
                line2_points.append(point)
        elif j[0] == "R":
            n = int(j[1:])
            for i in range(n):
                y = y + 1
                point = [x, y]
                line2_points.append(point)
        if j[0] == "L":
            n = int(j[1:])
            for i in range(n):
                y = y - 1
                point = [x, y]
                line2_points.append(point)
    closest_meeting = 1000000000000
    for j in line1_points:
        if j in line2_points:
            n = abs(j[0]) + abs(j[1])
            if n < closest_meeting:
                closest_meeting = n
    print(closest_meeting)