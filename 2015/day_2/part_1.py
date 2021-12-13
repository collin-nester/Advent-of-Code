#Advent of Code Day 2 Part 1
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
        h=c*d
        i=d*e
        j=c*e
        f=2*(h+i+j)
        if h<=i and h<=j:
            g=h+g
        elif i<=h and i<=j:
            g=i+g
        elif j<=h and j<=i:
            g=j+g
        g=g+f
        a=a+1
    print('The elves need '+str(g)+' square feet of wrapping paper.')

main()
