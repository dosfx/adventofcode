import re

with open("input.txt") as file:
    rules = []
    while len(line := file.readline().strip()) > 0:
        l, r = line.split("|")
        rules.append(f"{r},.*{l}")
    reg = re.compile("|".join(rules))
    total = 0
    for updates in file.readlines():
        updates = updates.strip()
        if re.search(reg, updates) is None:
            nums = updates.split(",")
            total += int(nums[int(len(nums) / 2)])
    print(total)