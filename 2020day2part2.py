#Advent of Code Day 2 Part 2

def main():

    g=0
    y=0
    with open('2020day2input.txt', 'r') as reader:
        codes=reader.readlines()
    for x in codes:
        x=x.split('-')
        c=x[1]
        x=x[0]  #x is the first spot
        c=c.split(' ')
        d=c[1]
        d=d[0]  #d is the letter we are checking
        e=c[2]  #e is the potential passcode
        c=c[0]  #c is the second spot
        if e[int(x)-1]==d:
            g=g+1
        if e[int(c)-1]==d:
            g=g+1
        if g==1:
            y=y+1
        g=0
    print('There are '+str(y)+' correct codes.')

main()
