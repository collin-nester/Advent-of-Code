total = 0
cardTotals = []
import math

with open("day_4/input.txt", "r") as reader:
    inputList = reader.readlines()

for i in range(0, len(inputList)):
    inputList[i] = inputList[i][9:]
    inputList[i] = inputList[i].split("|")
    inputList[i][0] = inputList[i][0].split(" ")
    inputList[i][1] = inputList[i][1].split(" ")

for i in inputList:
    matchList = []
    hasList = []
    cardTotal = 0
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
                cardTotal *= 2
                if cardTotal == 0:
                    cardTotal += 1
    total += cardTotal
    if cardTotal != 0:
        cardTotals.append(math.log2(cardTotal) + 1)
    else:
        cardTotals.append(0)
print(cardTotals)
print(total)