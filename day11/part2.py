from itertools import combinations
with open("input.txt") as file:
    space = [line.strip() for line in file.readlines()]

width = len(space[0])

emptyRows = []
row = "." * width
for i,line in enumerate(space):
    if line == row:
        emptyRows.append(i)

emptyCols = []
for x in range(width):
    if all([line[x] == "." for line in space]):
        emptyCols.append(x)

galaxies = []
for y,line in enumerate(space):
    x = 0
    while (x := line.find("#", x)) >= 0:
        galaxies.append((x, y))
        x += 1

total = 0
for a,b in combinations(galaxies, 2):
    ax,ay = a
    bx,by = b
    dist = abs(by - ay) + abs(bx - ax)
    for col in emptyCols:
        if (ax < col and col < bx) or (bx < col and col < ax):
            dist += 999999
    for row in emptyRows:
        if (ay < row and row < by) or (by < row and row < ay):
            dist += 999999

    total += dist

print(total)