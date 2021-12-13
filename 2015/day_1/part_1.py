#Advent of Code Day 1 Part 1 2015
def main():
    with open('day1input.txt', 'r') as reader:
        bigList=reader.readlines()
    letter=bigList[0]
    x=0
    for m in range(0,len(letter)):
        if letter[m]=='(':
            x=x+1
        elif letter[m]==')':
            x=x-1
    print('Go to floor '+str(x))
    
main()
