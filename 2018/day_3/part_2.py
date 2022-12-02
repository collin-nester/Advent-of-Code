readable_claim_list = []
claimed_fabric = []
claimed_fabric_count = 0

def create_claim(claim):
    new_claim = []
    claim_id = claim.split(" @ ")
    new_claim.append(claim_id[0])
    y_dist = claim_id[1].split(",")
    new_claim.append(y_dist[0])
    x_dist = y_dist[1].split(":")
    new_claim.append(x_dist[0])
    height = x_dist[1].split("x")
    new_claim.append(height[0])
    width = height[1].replace("\n","")
    new_claim.append(width)

    return new_claim

for k in range(1000):
    claimed_fabric.append([])
    for j in range(1000):
        claimed_fabric[-1].append(0)

with open('2018/day_3/input.txt', 'r') as reader:
    claim_list = reader.readlines()

for i in claim_list:
    readable_claim_list.append(create_claim(i))

for i in readable_claim_list:
    dist_x = int(i[1])
    dist_y = int(i[2])
    width = int(i[3])
    height = int(i[4])
    for j in range(width):
        for k in range(height):
            claimed_fabric[dist_y + k - 2][dist_x + j - 2] = claimed_fabric[dist_y + k - 2][dist_x + j - 2] + 1

for i in readable_claim_list:
    singular_points = 0
    claim_id = i[0]
    dist_x = int(i[1])
    dist_y = int(i[2])
    width = int(i[3])
    height = int(i[4])
    for j in range(width):
        for k in range(height):
            if claimed_fabric[dist_y + k - 2][dist_x + j - 2] == 1:
                singular_points = singular_points + 1
    if singular_points == width * height:
        print(claim_id)