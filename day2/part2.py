import re

id_re = re.compile(r'Game (\d+):')
red_re = re.compile(r'(\d+) red')
green_re = re.compile(r'(\d+) green')
blue_re = re.compile(r'(\d+) blue')

def max_cube(line: str, pattern: re.Pattern) -> int:
    max = 0
    for match in re.finditer(pattern, line):
        cur = int(match.group(1))
        if cur > max:
            max = cur
    return max

total = 0
with open("input.txt") as file:
    for line in file:
        red = max_cube(line, red_re)
        green = max_cube(line, green_re)
        blue = max_cube(line, blue_re)
        total += red * green * blue
print(total)