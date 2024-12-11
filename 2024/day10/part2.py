from aoc_lib import IntGrid


grid = IntGrid.from_file("input.txt")

visited: dict[tuple[int, int], int] = dict()


def step(x: int, y: int) -> int:
    if (x, y) in visited:
        return visited[(x, y)]
    cell = grid.at(x, y)
    if cell == 9:
        visited[(x, y)] = 1
        return 1

    paths = 0
    if grid.at_none(x + 1, y) == cell + 1:
        paths += step(x + 1, y)
    if grid.at_none(x, y + 1) == cell + 1:
        paths += step(x, y + 1)
    if grid.at_none(x - 1, y) == cell + 1:
        paths += step(x - 1, y)
    if grid.at_none(x, y - 1) == cell + 1:
        paths += step(x, y - 1)
    visited[(x, y)] = paths
    return paths


total = 0
for (x, y, _) in grid.find(0):
    total += step(x, y)
print(total)
