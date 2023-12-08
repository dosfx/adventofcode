import re

with open("input.txt") as file:
    lines = [l.strip() for l in file]

stop = 0
total = 0
line_count = len(lines)
line_len = len(lines[0])
gear_re = re.compile(r"(\d+)?([*])(\d+)?")
num_re = re.compile(r"\d+")
for i in range(line_count):
    for match in re.finditer(gear_re, lines[i]):
        gears = []
        if match.group(1) is not None:
            gears.append(int(match.group(1)))
        if match.group(3) is not None:
            gears.append(int(match.group(3)))
        start = max(0, match.start(2) - 3)
        end = min(line_len, match.end(2) + 3)
        if i > 0:
            for num_match in re.finditer(num_re, lines[i - 1][start:end]):
                if 2 < num_match.end(0) and num_match.start(0) < 5:
                    gears.append(int(num_match.group(0)))
        if i < (line_count - 1):
            for num_match in re.finditer(num_re, lines[i + 1][start:end]):
                if 2 < num_match.end(0) and num_match.start(0) < 5:
                    gears.append(int(num_match.group(0)))
        if len(gears) == 2:
            total += gears[0] * gears[1]
print(total)