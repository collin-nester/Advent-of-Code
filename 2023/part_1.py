total = 0
REDCUBEMAX = 12
GREENCUBEMAX = 13
BLUECUBEMAX = 14

with open("day_2/input.txt", "r") as reader:
    inputList = reader.readlines()

for i in inputList:
    include = True
    parsedInput = i.split("; ")
    parsedInput[0] = parsedInput[0].split(": ")[1]
    for j, k in enumerate(parsedInput):
        parsedInput[j] = k.split(", ")
        for l in parsedInput[j]:
            if ("red" in l and int(l.split(" ")[0]) > REDCUBEMAX) or ("blue" in l and int(l.split(" ")[0]) > BLUECUBEMAX) or ("green" in l and int(l.split(" ")[0]) > GREENCUBEMAX):
                include = False
    if include == True:
        print("true")
        total += int(i.split(":")[0][5:])
    print(parsedInput)

print(total)