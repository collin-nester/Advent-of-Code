#Advent of Code Day 3 Part 1
def main():
    with open('day3input.txt', 'r') as reader:
        bigList=reader.readlines()
    bigString=bigList[0]
    emptyList=[]
    a=0
    b=0
    e=0
    for x in range(0,len(bigString)):
        d=bigString[e]
        c=(str(a)+','+str(b))
        if d=='^':
            a=a+1
        if d=='v':
            a=a-1
        if d=='>':
            b=b+1
        if d=='<':
            b=b-1
        e=e+1
        if c not in emptyList:
            emptyList.append(c)
    print(len(emptyList))

main()
