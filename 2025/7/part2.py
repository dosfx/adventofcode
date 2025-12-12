import functools
from aoc_lib import StrGrid


grid = StrGrid.from_file("input.txt")

@functools.cache
def paths(x: int, y: int) -> int:
    assert(grid.at(x, y) == "^")
    left = 1
    for yy in range(y + 1, grid.height):
        if grid.at(x - 1, yy) == "^":
            left = paths(x - 1, yy)
            break
    right = 1
    for yy in range(y + 1, grid.height):
        if grid.at(x + 1, yy) == "^":
            right = paths(x + 1, yy)
            break
    return left + right

x, _ = next(grid.find("S"))
for y in range(0, grid.height):
    if grid.at(x, y) == "^":
        print(paths(x, y))
        break
