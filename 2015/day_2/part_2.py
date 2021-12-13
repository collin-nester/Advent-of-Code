#Advent of Code Day 2 Part 2
def main():
    with open('day2input.txt', 'r') as reader:
        bigList=reader.readlines()
    a=0
    g=0
    for y in bigList:
        b=bigList[a].split('x')
        c=b[0]
        d=b[1]
        e=b[2]
        e=e.replace('\n','')
        c=int(c)
        d=int(d)
        e=int(e)
        h=2*c+2*d
        i=2*d+2*e
        j=2*c+2*e
        f=c*d*e
        if h<=i and h<=j:
            g=h+g
        elif i<=h and i<=j:
            g=i+g
        elif j<=h and j<=i:
            g=j+g
        g=g+f
        a=a+1
    print('The elves need '+str(g)+' feet of ribbon.')

main()
