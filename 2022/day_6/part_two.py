x = 0
with open ("2022\day_6\input.txt", "r") as reader:
    datastream = reader.readline()

while x != -1:
    if datastream[x] not in datastream[x+1:x+14]:
        if datastream[x+1] not in datastream[x] + datastream[x+2:x+14]:
            if datastream[x+2] not in datastream[x:x+2] + datastream[x+3:x+14]:
                if datastream[x+3] not in datastream[x:x+3] + datastream[x+4:x+14]:
                    if datastream[x+4] not in datastream[x:x+4] + datastream[x+5:x+14]:
                        if datastream[x+5] not in datastream[x:x+5] + datastream[x+6:x+14]:
                            if datastream[x+6] not in datastream[x:x+6] + datastream[x+7:x+14]:
                                if datastream[x+7] not in datastream[x:x+7] + datastream[x+8:x+14]:
                                    if datastream[x+8] not in datastream[x:x+8] + datastream[x+9:x+14]:
                                        if datastream[x+9] not in datastream[x:x+9] + datastream[x+10:x+14]:
                                            if datastream[x+10] not in datastream[x:x+10] + datastream[x+11:x+14]:
                                                if datastream[x+11] not in datastream[x:x+11] + datastream[x+12:x+14]:
                                                    if datastream[x+12] not in datastream[x:x+12] + datastream[x+13]:
                                                        print(x + 14)
                                                        x = -2
    x = x + 1