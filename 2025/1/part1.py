cur = 50
count = 0
with open("input.txt") as f:
    for line in f.readlines():
        if line[0] == "R":
            cur += int(line[1:])
        else:
            cur -= int(line[1:])
        cur = cur % 100
        if cur == 0:
            count += 1
print(count)
