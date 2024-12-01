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

emptyRows.reverse()
for i in emptyRows:
    space.insert(i, row)
emptyCols.reverse()
for i in emptyCols:
    for y,line in enumerate(space):
        space[y] = f"{line[0:i]}.{line[i:]}"

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
    total += abs(by - ay) + abs(bx - ax)

print(total)