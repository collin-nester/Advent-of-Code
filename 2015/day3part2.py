#Advent of Code Day 3 Part 2
def main():
    with open('day3input.txt', 'r') as reader:
        bigList=reader.readlines()
    bigString=bigList[0]
    emptyList=[]
    a=0
    b=0
    e=0
    f=0
    g=0
    h=0
    for x in range(0,len(bigString)):
        d=bigString[e]
        if x%2==0:
            c=(str(a)+','+str(b))
            if d=='^':
                a=a+1
            if d=='v':
                a=a-1
            if d=='>':
                b=b+1
            if d=='<':
                b=b-1
            if c not in emptyList:
                emptyList.append(c)
        if x%2==1:
            h=(str(f)+','+str(g))
            if d=='^':
                f=f+1
            if d=='v':
                f=f-1
            if d=='>':
                g=g+1
            if d=='<':
                g=g-1
            if h not in emptyList:
                emptyList.append(h)
        e=e+1
    print(len(emptyList))

main()
