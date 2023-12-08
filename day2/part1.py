import re

id_re = re.compile(r'Game (\d+):')
red_re = re.compile(r'(\d+) red')
green_re = re.compile(r'(\d+) green')
blue_re = re.compile(r'(\d+) blue')

def check(line: str, pattern: re.Pattern, max: int) -> bool:
    for match in re.finditer(pattern, line):
        if int(match.group(1)) > max:
            return False
    return True

total = 0
with open("input.txt") as file:
    for line in file:
        if (check(line, red_re, 12) and check(line, green_re, 13) and check(line, blue_re, 14)):
            total += int(re.match(id_re, line).group(1))
print(total)