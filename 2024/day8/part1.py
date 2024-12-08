import itertools
import re

with open("input.txt") as file:
    grid = [line.strip() for line in file.readlines()]

width = len(grid[0])
height = len(grid)

Point = tuple[int, int]
antennas: dict[str, list[Point]] = {}
for match in re.finditer(r"[^.]", "".join(grid)):
    ant = match.group(0)
    if not ant in antennas:
        antennas[ant] = []
    antennas[ant].append((match.start() % width, int(match.start() / height)))

nodes: set[Point] = set()
for ant, points in antennas.items():
    for (a, b) in itertools.combinations(points, 2):
        diff = (b[0] - a[0], b[1] - a[1])
        p = (a[0] - diff[0], a[1] - diff[1])
        if 0 <= p[0] and p[0] < width and 0 <= p[1] and p[1] < height:
            nodes.add(p)
        p = (b[0] + diff[0], b[1] + diff[1])
        if 0 <= p[0] and p[0] < width and 0 <= p[1] and p[1] < height:
            nodes.add(p)
print(len(nodes))