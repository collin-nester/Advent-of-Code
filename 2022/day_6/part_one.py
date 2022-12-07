x = 0
with open ("2022\day_6\input.txt", "r") as reader:
    datastream = reader.readline()

while x != -1:
    if datastream[x] not in datastream[x+1:x+4]:
        if datastream[x+1] not in datastream[x] + datastream[x+2:x+4]:
            if datastream[x+2] not in datastream[x:x+2] + datastream[x+3]:
                if datastream[x+3] not in datastream[x:x+3]:
                    print(x + 4)
                    x = -2
    x = x + 1