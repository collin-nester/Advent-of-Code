quantity = [1] * 205

with open("day_4/input.txt", "r") as reader:
    inputList = reader.readlines()

for i in range(0, len(inputList)):
    inputList[i] = inputList[i][9:]
    inputList[i] = inputList[i].split("|")
    inputList[i][0] = inputList[i][0].split(" ")
    inputList[i][1] = inputList[i][1].split(" ")

for k, i in enumerate(inputList):
    matchList = []
    hasList = []
    matched = 0
    for j in i[0]:
        if j != "":
            j.removesuffix("\n")
            matchList.append(int(j))
    for j in i[1]:
        if j != "":
            j.removesuffix("\n")
            hasList.append(int(j))
    for i in matchList:
        for j in hasList:
            if i == j:
                matched += 1
    for n in range(k + 1, k + matched + 1):
        quantity[n] += quantity[k]

print(quantity)
total = 0
for i in quantity:
    total += i
print(total)