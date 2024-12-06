
with open("input.txt") as file:
    grid = [line.strip() for line in file.readlines()]

width = len(grid[0])
height = len(grid)
index = "".join(grid).find("^")
x = index % width
y = int(index / height)
direction = 0

visits: list[tuple[int, int]] = [(x, y)]
while True:
    nx = x
    ny = y
    if direction == 0:
        ny -= 1
    elif direction == 1:
        nx += 1
    elif direction == 2:
        ny += 1
    elif direction == 3:
        nx -= 1
    else:
        raise Exception(f"invalid dir: {direction}")
    if nx < 0 or width <= nx or ny < 0 or height <= ny:
        break
    if grid[ny][nx] == "#":
        direction = (direction + 1) % 4
        continue
    x = nx
    y = ny
    visits.append((nx, ny))
print(len(set(visits)))

