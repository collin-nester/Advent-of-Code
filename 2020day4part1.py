#Advent of Code Day 4 Part 1

def main():
    with open('2020day4input.txt', 'r') as reader:
        bigList=reader.read()
    bigList=bigList.split('\n\n')
    x=0
    for n in bigList:
        if 'byr' in n:
            if 'iyr' in n:
                if 'eyr' in n:
                    if 'hgt' in n:
                        if 'hcl' in n:
                            if 'ecl' in n:
                                if 'pid' in n:
                                    x=x+1
    print('There are '+str(x)+' valid passports.')
main()
