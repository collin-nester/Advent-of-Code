total = 0

with open("day_2/input.txt", "r") as reader:
    inputList = reader.readlines()

for i in inputList:
    redmax = 0
    greenmax = 0
    bluemax = 0
    parsedInput = i.split("; ")
    parsedInput[0] = parsedInput[0].split(": ")[1]

    for j, k in enumerate(parsedInput):
        parsedInput[j] = k.split(", ")
        for l in parsedInput[j]:
            num = int(l.split(" ")[0])
            if "red" in l and num > redmax:
                redmax = num
            if "green" in l and num > greenmax:
                greenmax = num
            if "blue" in l and num > bluemax:
                bluemax = num
    print(str(redmax) + " " + str(bluemax) + " " + str(greenmax))
    total += redmax * greenmax * bluemax

print(total)
