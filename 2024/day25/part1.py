with open("input.txt") as file:
    keys = list[list[int]]()
    locks = list[list[int]]()
    while len(line := file.readline()) > 0:
        line = line.strip()
        iskey = line == "#####"
        block = [0] * 5 if iskey else [-1] * 5
        for _ in range(6):
            for i, c in enumerate(file.readline().strip()):
                if c == "#":
                    block[i] += 1
        file.readline()
        if iskey:
            keys.append(block)
        else:
            locks.append(block)

total = 0
for key in keys:
    for lock in locks:
        for i in range(5):
            if key[i] + lock[i] > 5:
                break
        else:
            total += 1
print(total)