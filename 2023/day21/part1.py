with open("input.txt") as file:
    grid = []
    for y,line in enumerate(file.readlines()):
        if "S" in line:
            start = (line.index("S"), y)
        grid.append([c for c in line.strip()])
WIDTH = len(grid[0])
HEIGHT = len(grid)

def dump(steps):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print("O" if (x, y) in steps else grid[y][x], end="")
        print()

def can_step(x, y):
    if x < 0 or WIDTH <= x or y < 0 or HEIGHT <= y:
        return False
    return grid[y][x] == "."

grid[start[1]][start[0]] = "."
last = set([start])
for i in range(64):
    cur = set()
    for x, y in last:
        temp = (x + 1, y)
        if can_step(*temp):
            cur.add(temp)
        temp = (x - 1, y)
        if can_step(*temp):
            cur.add(temp)
        temp = (x, y + 1)
        if can_step(*temp):
            cur.add(temp)
        temp = (x, y - 1)
        if can_step(*temp):
            cur.add(temp)
    last = cur
    # dump(cur)
    # print()
print(len(cur))