#Advent of Code Day 3 Part 1

numbersList=[]

def main(c,d):

        with open('2020day3input.txt', 'r') as reader:
            bigList=reader.readlines()
        r=1
        x=0
        e=1
        for w in bigList:
            w=w.strip()
            f=e%2
            if f==1:
                if r!=1:
                    m=len(w)
                    k=r%m
                    if w[int(k)-1]=='#':
                        x=x+1
                r=r+d
            if c==2:
                e=e+1
        numbersList.append(x)

main(1,1)
main(1,3)
main(1,5)
main(1,7)
main(2,1)

print(numbersList[0]*numbersList[1]*numbersList[2]*numbersList[3]*numbersList[4])
for k in numbersList:
    print(k)
