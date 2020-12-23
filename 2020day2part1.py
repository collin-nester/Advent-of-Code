#Advent of Code Day 2 Part 1

def main():

    g=0
    b=0
    z='false'
    y=0
    with open('day2input.txt', 'r') as reader:
        codes=reader.readlines()
    for x in codes:
        x=x.split('-')
        c=x[1]
        x=x[0]  #x is the minimum
        c=c.split(' ')
        d=c[1]
        d=d[0]  #d is the letter we are checking
        e=c[2]  #e is the potential passcode
        c=c[0]  #c is the maximum
        b=b+1
        for f in e:
            if f==d:
                g=g+1
        if g>=int(x) and g<=int(c):
            y=y+1
            print(e)
        g=0
        b=0
        z='false'
    print('There are '+str(y)+' correct codes.')

main()
