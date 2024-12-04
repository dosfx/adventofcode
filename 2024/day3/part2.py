import re

with open("input.txt") as file:
    total = 0
    skip = False
    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", "\n".join(file.readlines())):
        if str(match.group(0)) == "do()":
            skip = False
            continue
        if str(match.group(0)) == "don't()":
            skip = True
            continue
        if skip: continue
        l, r = [int(num) for num in match.groups()]
        total += l * r
    print(total)