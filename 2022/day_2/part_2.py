readable_strategy_guide = []
p_one = ""
p_two = ""
point_total = 0

with open ('2022/day_2/input.txt', 'r') as reader:
    strategy_guide = reader.readlines()

for i in strategy_guide:
    i = i.replace("\n", "")
    readable_strategy_guide.append(i.split(" "))

for j in readable_strategy_guide:
    if j[0] == "A":
        p_one = "rock"
    elif j[0] == "B":
        p_one = "paper"
    else:
        p_one = "scissors"

    if j[1] == "Z":
        p_two = "win"
        point_total = point_total + 6

        if p_one == "rock":
            point_total = point_total + 2
        elif p_one == "paper":
            point_total = point_total + 3
        else:
            point_total = point_total + 1

    elif j[1] == "Y":
        p_two = "draw"
        point_total = point_total + 3

        if p_one == "rock":
            point_total = point_total + 1
        elif p_one == "paper":
            point_total = point_total + 2
        else:
            point_total = point_total + 3

    else:
        p_two = "loss"

        if p_one == "rock":
            point_total = point_total + 3
        elif p_one == "paper":
            point_total = point_total + 1
        else:
            point_total = point_total + 2
    
    
    
print(point_total)