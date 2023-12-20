DELTA = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}

with open("input.txt") as file:
    plans = []
    x = y = minx = miny = maxx = maxy = 0
    for line in file.readlines():
        [direction, num] = line.split(" ")[0:2]
        num = int(num)
        plans.append((direction, num))
        (dx, dy) = DELTA[direction]
        x += num * dx
        y += num * dy
        minx = min(minx, x)
        maxx = max(maxx, x)
        miny = min(miny, y)
        maxy = max(maxy, y)

width = maxx - minx + 1
height = maxy - miny + 1

grid = []
for y in range(height):
    grid.append(["."] * width)

total = 0
x = minx * -1
y = miny * -1
grid[y][x] = "#"
for (direction, num) in plans:
    total += num
    (dx, dy) = DELTA[direction]
    for i in range(num):
        x += dx
        y += dy
        grid[y][x] = "#"

for y in range(height):
    for x in range(1, width):
        if grid[y][x] == "." and grid[y][x - 1] == "#" and (x < 2 or grid[y][x - 2] == "."):
            break
    else:
        continue
    break

steps = [(x, y)]
while len(steps) > 0:
    (x, y) = steps.pop()
    if x < 0 or width <= x or y < 0 or height <= y:
        continue
    if grid[y][x] == "#":
        continue
    if grid[y][x] == "-":
        continue
    grid[y][x] = "-"
    total += 1
    steps.append((x - 1, y))
    steps.append((x + 1, y))
    steps.append((x, y - 1))
    steps.append((x, y + 1))

print(total)

with open("output.txt", "w") as file:
    for row in grid:
        file.write("".join(row))
        file.write("\n")
