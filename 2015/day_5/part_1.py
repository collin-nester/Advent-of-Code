#Advent of Code Day 5 Part 1
def main():
    a=0
    with open('day5input.txt', 'r') as reader:
        bigList=reader.readlines()
    for b in bigList:
        c=b.count('a')
        d=b.count('e')
        e=b.count('i')
        f=b.count('o')
        g=b.count('u')
        if 'ab' in b:
            a=a-1
        elif 'cd' in b:
            a=a-1
        elif 'pq' in b:
            a=a-1
        elif 'xy' in b:
            a=a-1
        elif c+d+e+f+g<3:
            a=a-1
        elif 'aa' not in b and 'bb' not in b and 'cc' not in b and 'dd' not in b and 'ee' not in b and 'ff' not in b and 'gg' not in b and 'hh' not in b and 'ii' not in b and 'jj' not in b and 'kk' not in b and 'll' not in b and 'mm' not in b and 'nn' not in b and 'oo' not in b and 'pp' not in b and 'qq' not in b and 'rr' not in b and 'ss' not in b and 'tt' not in b and 'uu' not in b and 'vv' not in b and 'ww' not in b and 'xx' not in b and 'yy' not in b and 'zz' not in b:
            a=a-1
        a=a+1
    print(a)
main()
