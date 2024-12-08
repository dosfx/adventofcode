import itertools
import re

from lib import Point2

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
        nodes.add(a)
        v = diff
        while True:
            p = (a[0] + v[0], a[1] + v[1])
            if p[0] < 0 or width <= p[0] or p[1] < 0 or height <= p[1]:
                break
            nodes.add(p)
            v = (v[0] + diff[0], v[1] + diff[1])
        v = (-diff[0], -diff[1])
        while True:
            p = (a[0] + v[0], a[1] + v[1])
            if p[0] < 0 or width <= p[0] or p[1] < 0 or height <= p[1]:
                break
            nodes.add(p)
            v = (v[0] - diff[0], v[1] - diff[1])
print(len(nodes))