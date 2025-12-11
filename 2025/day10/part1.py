import pprint

with open ("2025/day10/input.txt", "r") as reader:
    input = reader.readlines()

def process_line(line):
    split_line = line.split(" ")
    raw_lights = split_line[0][1:-1]
    lights = [0] * len(raw_lights)
    for light_number, light in enumerate(raw_lights):
        lights[light_number] = int(light == '#')
    buttons = []
    for button in split_line[1:-1]:
        button_nums = []
        for num in button[1:-1].split(","):
            button_nums.append(int(num))
        buttons.append(button_nums)
    joltages = []
    for joltage in split_line[-1].strip()[1:-1].split(","):
        joltages.append(int(joltage))
    return lights, buttons, joltages

def solves_lights(lights, buttons, button_sequence):
    light_simu = [0] * len(lights)
    for press in button_sequence:
        light_simu = press_button(light_simu, buttons[press])
    for light_number, light in enumerate(lights):
        matches = int(abs(light_simu[light_number]-light)<0.1)
        if not matches:
            return False
    return True

def press_button(lights, button):
    for light in button:
        lights[light] = int(lights[light]==0)
    return lights

def light_to_str(lights):
    lights_str = ""
    for light in lights:
        lights_str += str(light)
    return lights_str

def str_to_lights(str):
    lights_array = []
    for num in str:
        lights_array.append(int(num))
    return lights_array


total = 0
for line in input:
    lights, buttons, joltages = process_line(line)
    start_pos = [0] * len(lights)
    branches_start = {light_to_str(start_pos)}
    start_depth = 0
    end_pos = lights
    branches_end = {light_to_str(end_pos)}
    end_depth = 0
    met = False
    num_presses = 0
    while not met:
        branches_to_add = []
        for lights in branches_start:
            for button in buttons:
                branches_to_add.append(light_to_str(press_button(str_to_lights(lights), button)))
        for branch in branches_to_add:
            branches_start.add(branch)
        start_depth += 1
        if len(branches_start|branches_end) != len(branches_start) + len(branches_end):
            met = True
            num_presses = start_depth + end_depth
            break
        branches_to_add = []
        for lights in branches_end:
            for button in buttons:
                branches_to_add.append(light_to_str(press_button(str_to_lights(lights), button)))
        for branch in branches_to_add:
            branches_end.add(branch)
        end_depth += 1
        if len(branches_start|branches_end) != len(branches_start) + len(branches_end):
            met = True
            num_presses = start_depth + end_depth
            break
    total += num_presses

print(total)