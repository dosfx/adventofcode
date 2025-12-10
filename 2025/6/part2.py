with open("input.txt") as f:
    lines = f.readlines()

ops = lines[-1].split()
total = 0
opsIndex = 0
cur = 0 if ops[opsIndex] == "+" else 1
for i in range(len(lines[0]) - 1):
    num = 0
    for line in lines[:-1]:
        c = line[i]
        if c != " ":
            num = (num * 10) + int(c)
    if num == 0:
        # next!
        opsIndex += 1
        total += cur
        cur = 0 if ops[opsIndex] == "+" else 1
        continue
    if ops[opsIndex] == "+":
        cur += num
    else:
        cur *= num

print(total + cur)
