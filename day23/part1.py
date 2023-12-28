from typing import Dict, List, Tuple

Point = Tuple[int, int]

with open("input.txt") as file:
    grid = [line.strip() for line in file.readlines()]

slopes = {
    "^": 0,
    "v": 1,
    "<": 2,
    ">": 3,
}
width = len(grid[0])
height = len(grid)
best = ()
stack: List[Tuple[Point, ...]] = []
stack.append(((1, 0),))
while len(stack) > 0:
    cur = stack.pop()
    p = cur[-1]
    x, y = p
    if x < 0 or width <= x or y < 0 or height <= y:
        continue
    if x == width - 2 and y == height - 1:
        # done
        print("end", len(cur) - 1)
        if len(best) < len(cur):
            best = cur
            print("new best")
        continue
    c = grid[y][x]
    if c == "#":
        continue
    dirs: List[Point] = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
    if c in slopes:
        d = dirs[slopes[c]]
        if d not in cur:
            stack.append(cur + (d,))
        continue
    for d in dirs:
        if not d in cur:
            stack.append(cur + (d,))

# for y in range(height):
#     for x in range(width):
#         print("O" if (x,y) in best else grid[y][x], end="")
#     print()