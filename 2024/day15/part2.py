from aoc_lib import StrGrid, Vector2, DOWN, LEFT, RIGHT, UP


with open("input.txt") as file:
    lines = []
    while len(line := file.readline().strip()) > 0:
        lines.append(line.replace("#", "##").replace(
            "O", "[]").replace(".", "..").replace("@", "@."))
    moves = "".join([line.strip() for line in file.readlines()])
grid = StrGrid(lines)

move_table = {
    "^": UP,
    ">": RIGHT,
    "v": DOWN,
    "<": LEFT,
}


def push(p: Vector2, d: Vector2, swap: bool = True) -> bool:
    cell = grid.atp(p)
    if cell == ".":
        return True
    if cell == "#":
        return False
    if d.horizonal:
        if not push(p + d + d, d):
            return False
        grid.swapp(p + d + d, p + d)
        grid.swapp(p + d, p)
        return True
    if cell == "[":
        left = p
        right = p + RIGHT
    else:
        right = p
        left = p + LEFT
    if not push(left + d, d, False) or not push(right + d, d, False):
        return False
    if swap:
        push(left + d, d)
        push(right + d, d)
        grid.swapp(left, left + d)
        grid.swapp(right, right + d)
    return True


cur = [Vector2(x, y) for x, y, _ in grid.findr("@")][0]
for m in moves:
    direction = move_table[m]
    nextp = cur + direction
    cell = grid.atp(nextp)
    if cell == "#":
        continue
    if cell == ".":
        grid.swapp(cur, nextp)
        cur = nextp
        continue
    assert cell == "[" or cell == "]"
    if push(nextp, direction):
        grid.swapp(cur, nextp)
        cur = nextp

total = 0
for x, y, _ in grid.findr(r"\["):
    total += x + (100 * y)
print(total)