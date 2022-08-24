#Advent of Code Day 1 Part 2 2015
def main():
    with open('2015/day_1/input.txt', 'r') as reader:
        bigList=reader.readlines()
    letter=bigList[0]
    x=0
    y=0
    z=0
    for m in range(0,len(letter)):
        if letter[m]=='(':
            x=x+1
        elif letter[m]==')':
            x=x-1
        if x==-1 and z!=-1:
            z=-1
            y=m+1
    print('He reaches the basement at '+str(y))
    
main()
