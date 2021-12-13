#Advent of Code Day 4 Part 1
import hashlib
def main():
    with open('day4input.txt', 'r') as reader:
        bigList=reader.readlines()
    x=str(bigList)
    a=x
    c=1
    d=0
    while a[:6]!='000000':
        b=x+str(c)
        b=b.replace("['",'')
        b=b.replace("']",'')
        a=hashlib.md5(b.encode())
        c=c+1
        a=a.hexdigest()
    print(b)
    print(a)


main()
