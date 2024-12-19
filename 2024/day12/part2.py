from aoc_lib import DIRECTIONS, Vector2, StrGrid

grid = StrGrid.from_file("input.txt")


def fill(id: str, p: Vector2, cur: set[Vector2]) -> None:
    if p in cur:
        return
    if grid.atp_none(p) != id:
        return
    cur.add(p)
    for d in DIRECTIONS:
        fill(id, p + d, cur)


def edge_walk(region: set[Vector2], start: Vector2, side: Vector2) -> set[Vector2]:
    edge = {start}
    for check_dir in [side.clock, side.counter]:
        check = start + check_dir
        while check in region and (check + side) not in region:
            edge.add(check)
            check = check + check_dir
    return edge


total = 0
visited: set[Vector2] = set()
for x, y, cell in grid.cells():
    p = Vector2(x, y)
    if p in visited:
        continue
    region: set[Vector2] = set()
    fill(cell, p, region)
    visited = visited.union(region)

    edges = 0
    used: dict[Vector2, set[Vector2]] = {d: set() for d in DIRECTIONS}
    for p in region:
        for d in DIRECTIONS:
            if not (p + d) in region:
                # found an edge
                if p not in used[d]:
                    edges += 1
                    used[d] = used[d].union(edge_walk(region, p, d))

    total += len(region) * edges
print(total)
