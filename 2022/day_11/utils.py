import re

def first_int(string):
    return int(re.findall(r"(?:(?<!\d)-)?\d+", string)[0])

def ints(string):
    return re.findall(r"(?:(?<!\d)-)?\d+", string)