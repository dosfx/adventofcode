import re

with open("input.txt") as file:
    total = 0
    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", "\n".join(file.readlines())):
        l, r = [int(num) for num in match.groups()]
        total += l * r
    print(total)