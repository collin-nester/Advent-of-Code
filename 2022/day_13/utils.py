import re

def first_int(string):
    return int(re.findall(r"(?:(?<!\d)-)?\d+", string)[0])

def ints(string):
    return re.findall(r"(?:(?<!\d)-)?\d+", string)

def alpha_set():
    return ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")