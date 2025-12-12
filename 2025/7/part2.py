import functools
from aoc_lib import StrGrid


grid = StrGrid.from_file("input.txt")


@functools.cache
def paths(x: int, y: int) -> int:
    c = grid.at_none(x, y)
    if c is None:
        return 1
    if c == "." or c == "S":
        return paths(x, y + 1)
    return paths(x - 1, y) + paths(x + 1, y)


print(paths(*next(grid.find("S"))))
