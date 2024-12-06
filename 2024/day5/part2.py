import re

with open("input.txt") as file:
    reg_rules = []
    sort_rules: set[str] = set()
    while len(line := file.readline().strip()) > 0:
        sort_rules.add(line)
        l, r = line.split("|")
        reg_rules.append(f"{r},.*{l}")
    reg = re.compile("|".join(reg_rules))
    bad = []
    for updates in file.readlines():
        updates = updates.strip()
        if re.search(reg, updates) is not None:
            bad.append(updates)

class Node:
    def __init__(self, num: str):
        self.num = num

    def __lt__(self, other: "Node") -> bool:
        return f"{self.num}|{other.num}" in sort_rules

    def __repr__(self) -> str:
        return self.num

total = 0
for fix in bad:
    fixed = sorted([Node(num) for num in fix.split(",")])
    total += int(fixed[int(len(fixed) / 2)].num)
print(total)