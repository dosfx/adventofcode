with open("input.txt") as f:
    lines = f.readlines()

ops = lines[-1].split()
totals: list[int] = [int(col) for col in lines[0].split()]
for line in lines[1:-1]:
    for i, col in enumerate(line.split()):
        if ops[i] == "*":
            totals[i] *= int(col)
        else:
            totals[i] += int(col)
print(sum(totals))
