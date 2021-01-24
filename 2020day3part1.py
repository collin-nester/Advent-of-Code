#Advent of Code Day 3 Part 1

def main():

        with open('2020day3input.txt', 'r') as reader:
            bigList=reader.readlines()
        r=1
        x=0
        for w in bigList:
            w=w.strip()
            if r!=1:
                m=len(w)
                k=r%m
                if w[int(k)-1]=='#':
                    x=x+1
            r=r+3
        print(x)

main()
