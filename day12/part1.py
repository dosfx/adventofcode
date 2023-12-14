from itertools import product
import re

with open("input.txt") as file:
    lines = file.readlines()

total = 0
for row,line in enumerate(lines):
    sub = 0
    [springs, check] = line.split()
    re_check = re.compile("^[.]*" + "[.]+".join([f"#{{{c}}}" for c in check.split(",")]) + "[.]*$")
    for perm in product(".#", repeat=springs.count("?")):
        i = 0
        generate = []
        for c in springs:
            if c == "?":
                generate.append(perm[i])
                i += 1
            else:
                generate.append(c)
        generate = "".join(generate)
        if re.match(re_check, generate) is not None:
            sub += 1
    print(row, springs, check, sub)
    total += sub
print(total)