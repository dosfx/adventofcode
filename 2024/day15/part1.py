from aoc_lib import StrGrid, Vector2, DOWN, LEFT, RIGHT, UP


with open("input.txt") as file:
    lines = []
    while len(line := file.readline().strip()) > 0:
        lines.append(line)
    moves = "".join([line.strip() for line in file.readlines()])
grid = StrGrid(lines)

move_table = {
    "^": UP,
    ">": RIGHT,
    "v": DOWN,
    "<": LEFT,
}

cur = [Vector2(x, y) for x, y, _ in grid.find("@")][0]
for m in moves:
    # print(grid, m)
    direction = move_table[m]
    next_p = cur + direction
    cell = grid.atp(next_p)
    if cell == "#":
        continue
    if cell == ".":
        grid.swapp(next_p, cur)
        cur = next_p
        continue
    assert cell == "O"
    search = next_p
    while True:
        search += direction
        cell = grid.atp(search)
        if cell == "O":
            # keep looking
            continue
        if cell == ".":
            # shift
            while search != cur:
                grid.swapp(search, search - direction)
                search -= direction
            cur = next_p
        break

total = 0
for x, y, _ in grid.find("O"):
    total += x + (100 * y)
print(total)