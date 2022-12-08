directory_list = [0]
x = 0
sum_of_directories = 0
directory_sum = 0
sum_list = []

def add_list():
    global x
    if x == 0:
        a = [0]
        directory_list.append(a)
        sum_list.append(a)
    elif x == 1:
        b = [0]
        directory_list[-1].append(b)
        sum_list.append(b)
    elif x == 2:
        c = [0]
        directory_list[-1][-1].append(c)
        sum_list.append(c)
    elif x == 3:
        e = [0]
        directory_list[-1][-1][-1].append(e)
        sum_list.append(e)
    elif x == 4:
        ftopayrespects = [0]
        directory_list[-1][-1][-1][-1].append(ftopayrespects)
        sum_list.append(ftopayrespects)
    elif x == 5:
        g = [0]
        directory_list[-1][-1][-1][-1][-1].append(g)
        sum_list.append(g)
    elif x == 6:
        h = [0]
        directory_list[-1][-1][-1][-1][-1][-1].append(h)
        sum_list.append(h)
    elif x == 7:
        iinrange = [0]
        directory_list[-1][-1][-1][-1][-1][-1][-1].append(iinrange)
        sum_list.append(iinrange)
    elif x == 8:
        k = [0]
        directory_list[-1][-1][-1][-1][-1][-1][-1][-1].append(k)
        sum_list.append(k)
    elif x == 9:
        lmnop = [0]
        directory_list[-1][-1][-1][-1][-1][-1][-1][-1][-1].append(lmnop)
        sum_list.append(lmnop)
    else:
        qrstuvwxyzandalsodandj = [0]
        directory_list[-1][-1][-1][-1][-1][-1][-1][-1][-1][-1].append(qrstuvwxyzandalsodandj)
        sum_list.append(qrstuvwxyzandalsodandj)

def organize_files():
    global x
    for i in terminal_data:
        if "$ cd" in i:
            if "/" in i:
                x = 0
            elif ".." in i:
                x = x - 1
            else:
                add_list()
                x = x + 1

        elif i[0].isdigit():
            size = int(i.split(" ")[0])
            if x == 0:
                directory_list[0] += size
            elif x == 1:
                directory_list[-1][0] += size
                directory_list[0] += size
            elif x == 2:
                directory_list[-1][-1][0] += size
                directory_list[-1][0] += size
                directory_list[0] += size
            elif x == 3:
                directory_list[-1][-1][-1][0] += size
                directory_list[-1][-1][0] += size
                directory_list[-1][0] += size
                directory_list[0] += size
            elif x == 4:
                directory_list[-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][0] += size
                directory_list[-1][-1][0] += size
                directory_list[-1][0] += size
                directory_list[0] += size
            elif x == 5:
                directory_list[-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][0] += size
                directory_list[-1][-1][0] += size
                directory_list[-1][0] += size
                directory_list[0] += size
            elif x == 6:
                directory_list[-1][-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][0] += size
                directory_list[-1][-1][0] += size
                directory_list[-1][0] += size
                directory_list[0] += size
            elif x == 7:
                directory_list[-1][-1][-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][0] += size
                directory_list[-1][-1][0] += size
                directory_list[-1][0] += size
                directory_list[0] += size
            if x == 8:
                directory_list[-1][-1][-1][-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][0] += size
                directory_list[-1][-1][0] += size
                directory_list[-1][0] += size
                directory_list[0] += size
            if x == 9:
                directory_list[-1][-1][-1][-1][-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][0] += size
                directory_list[-1][-1][0] += size
                directory_list[-1][0] += size
                directory_list[0] += size
            if x == 10:
                directory_list[-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][-1][0] += size
                directory_list[-1][-1][-1][0] += size
                directory_list[-1][-1][0] += size
                directory_list[-1][0] += size
                directory_list[0] += size

def add_to_total(directory_sum):
    global sum_of_directories
    if directory_sum[0] <= 100000:
        sum_of_directories += directory_sum[0]

def add_all_the_things():
    print(sum_list)
    for i in sum_list:
        add_to_total(i)

with open("2022/day_7/input.txt", "r") as reader:
    terminal_data = reader.readlines()

organize_files()
add_all_the_things()
print(sum_of_directories)