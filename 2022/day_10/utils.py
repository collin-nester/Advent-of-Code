import re

def first_int(string):
    return int(re.findall(r"(?:(?<!\d)-)?\d+", string)[0])