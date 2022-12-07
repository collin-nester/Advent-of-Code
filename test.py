import math
list = [1,2,3,4,5,[6,7,[8,9],[10,11]]]
number = 0
def add_directories(list):
    global number
    for i in list:
        if type(i) == int:
            number += i
        else:
            add_directories(i)
add_directories(list)
print(number)
x = 12
print((pow(x,2)-x)/2)