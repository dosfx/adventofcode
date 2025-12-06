cur = 50
count = 0
with open("input.txt") as f:
    for line in f.readlines():
        diff = 1 if line[0] == "R" else -1
        for _ in range(int(line[1:])):
            cur = (cur + diff) % 100
            if cur == 0:
                count += 1
print(count)
