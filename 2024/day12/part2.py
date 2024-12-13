from aoc_lib import Direction, Point2, StrGrid

grid = StrGrid.from_file("input.txt")


def fill(id: str, p: Point2, cur: set[Point2]) -> None:
    if p in cur:
        return
    if grid.atp_none(p) != id:
        return
    cur.add(p)
    for d in Direction:
        fill(id, p.shift(d), cur)


def edge_walk(region: set[Point2], start: Point2, side: Direction) -> set[Point2]:
    edge = {start}
    for check_dir in [side.clock(), side.counter()]:
        check = start.shift(check_dir)
        while check in region and check.shift(side) not in region:
            edge.add(check)
            check = check.shift(check_dir)
    return edge


total = 0
visited: set[Point2] = set()
for x, y, cell in grid.cells():
    p = Point2(x, y)
    if p in visited:
        continue
    region: set[Point2] = set()
    fill(cell, p, region)
    visited = visited.union(region)

    edges = 0
    used: dict[Direction, set[Point2]] = {d: set() for d in Direction}
    for p in region:
        for d in Direction:
            if not p.shift(d) in region:
                # found an edge
                if p not in used[d]:
                    edges += 1
                    used[d] = used[d].union(edge_walk(region, p, d))

    total += len(region) * edges
print(total)

# RRRR
# RRRR
#   RRR
#   R
