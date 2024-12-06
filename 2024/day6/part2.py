
with open("input.txt") as file:
    grid = [line.strip() for line in file.readlines()]

width = len(grid[0])
height = len(grid)
index = "".join(grid).find("^")
startx = index % width
starty = int(index / height)

def path(extra: tuple[int, int] | None = None) -> tuple[bool, set[tuple[int, int, int]]]:
    x = startx
    y = starty
    d = 0
    visits: set[tuple[int, int, int]] = set([(x, y, d)])
    while True:
        nx = x
        ny = y
        if d == 0:
            ny -= 1
        elif d == 1:
            nx += 1
        elif d == 2:
            ny += 1
        elif d == 3:
            nx -= 1
        else:
            raise Exception(f"invalid dir: {d}")
        if nx < 0 or width <= nx or ny < 0 or height <= ny:
            break
        if grid[ny][nx] == "#" or extra == (nx, ny):
            d = (d + 1) % 4
            continue
        x = nx
        y = ny
        if (x, y, d) in visits:
            return (True, set())
        visits.add((x, y, d))
    return (False, visits)

_, possible_extras = path()
count = 0
for (x, y) in set([(x, y) for (x, y, _) in possible_extras]):
    if startx == x and starty == y:
        continue
    if path((x, y))[0]:
        count += 1
print(count)

# 6 7
# 7 9
# 3 6
# 7 7
# 3 8
# 1 8