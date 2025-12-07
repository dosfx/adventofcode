import re

with open("input.txt") as f:
    line = f.readline()

total = 0
reg = re.compile(r"^(\d+)\1+$")
for pair in line.split(","):
    a, b = [int(s) for s in pair.split("-")]
    for i in range(a, b + 1):
        if reg.match(str(i)) is not None:
            total += i
print(total)