from aoc_lib import Direction, Vector2, StrGrid

grid = StrGrid.from_file("input.txt")


def fill(id: str, p: Vector2, cur: set[Vector2]) -> None:
    if p in cur:
        return
    if grid.atp_none(p) != id:
        return
    cur.add(p)
    for d in Direction:
        fill(id, p.shift(d), cur)

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
        for d in Direction:
            if not p.shift(d) in region:
                perimeter += 1
    total += len(region) * perimeter
print(total)