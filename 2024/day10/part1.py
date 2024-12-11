from aoc_lib import IntGrid


grid = IntGrid.from_file("input.txt")

summit_set = set[tuple[int, int]]

visited: dict[tuple[int, int], summit_set] = dict()


def step(x: int, y: int) -> summit_set:
    if (x, y) in visited:
        return visited[(x, y)]
    cell = grid.at(x, y)
    if cell == 9:
        visited[(x, y)] = {(x, y)}
        return {(x, y)}

    paths: summit_set = set()
    if grid.at_none(x + 1, y) == cell + 1:
        paths = paths.union(step(x + 1, y))
    if grid.at_none(x, y + 1) == cell + 1:
        paths = paths.union(step(x, y + 1))
    if grid.at_none(x - 1, y) == cell + 1:
        paths = paths.union(step(x - 1, y))
    if grid.at_none(x, y - 1) == cell + 1:
        paths = paths.union(step(x, y - 1))
    visited[(x, y)] = paths
    return paths


total = 0
for (x, y, _) in grid.find(0):
    total += len(step(x, y))
print(total)
