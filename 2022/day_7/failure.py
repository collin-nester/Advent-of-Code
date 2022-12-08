directory_list = [0]
x = 0
sum_of_directories = 0
directory_sum = 0

def add_list():
    global x
    if x == 0:
        directory_list.append([0])
    elif x == 1:
        directory_list[-1].append([0])
    elif x == 2:
        directory_list[-1][-1].append([0])
    elif x == 3:
        directory_list[-1][-1][-1].append([0])
    elif x == 4:
        directory_list[-1][-1][-1][-1].append([0])
    elif x == 5:
        directory_list[-1][-1][-1][-1][-1].append([0])
    elif x == 6:
        directory_list[-1][-1][-1][-1][-1][-1].append([0])
    elif x == 7:
        directory_list[-1][-1][-1][-1][-1][-1][-1].append([0])
    elif x == 8:
        directory_list[-1][-1][-1][-1][-1][-1][-1][-1].append([0])
    elif x == 9:
        directory_list[-1][-1][-1][-1][-1][-1][-1][-1][-1].append([0])
    else:
        directory_list[-1][-1][-1][-1][-1][-1][-1][-1][-1][-1].append([0])

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
            elif x == 2:
                directory_list[-1][-1][0] += size
            elif x == 3:
                directory_list[-1][-1][-1][0] += size
            elif x == 4:
                directory_list[-1][-1][-1][-1][0] += size
            elif x == 5:
                directory_list[-1][-1][-1][-1][-1][0] += size
            elif x == 6:
                directory_list[-1][-1][-1][-1][-1][-1][0] += size
            elif x == 7:
                directory_list[-1][-1][-1][-1][-1][-1][-1][0] += size
            if x == 8:
                directory_list[-1][-1][-1][-1][-1][-1][-1][-1][0] += size
            if x == 9:
                directory_list[-1][-1][-1][-1][-1][-1][-1][-1][-1][0] += size

def add_directories(sample_list):
    global directory_sum
    for i in sample_list:
        if type(i) == int:
            directory_sum += i
            if len(sample_list) == 1:
                add_to_total(directory_sum)
                directory_sum = 0
        else:
            add_directories(i)
        
def add_to_total(directory_sum):
    global sum_of_directories
    if directory_sum <= 100000:
            sum_of_directories += directory_sum

def scan_for_small_directories(directorylist):
    for i in directorylist:
        if type(i) != int:
            scan_for_small_directories(i)
        else:
            add_directories(directorylist)


with open("2022/day_7/testinput.txt", "r") as reader:
    terminal_data = reader.readlines()

organize_files()
scan_for_small_directories(directory_list)
print(sum_of_directories)