from aoc_lib import DIRECTIONS, Vector2, StrGrid

grid = StrGrid.from_file("input.txt")


def fill(id: str, v: Vector2, cur: set[Vector2]) -> None:
    if v in cur:
        return
    if grid.atp_none(v) != id:
        return
    cur.add(v)
    for d in DIRECTIONS:
        fill(id, v + d, cur)


total = 0
visited: set[Vector2] = set()
for x, y, cell in grid.cells():
    p = Vector2(x, y)
    if p in visited:
        continue
    region: set[Vector2] = set()
    fill(cell, p, region)
    visited = visited.union(region)

    perimeter = 0
    for p in region:
        for d in DIRECTIONS:
            if not (p + d) in region:
                perimeter += 1
    total += len(region) * perimeter
print(total)
