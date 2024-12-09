import itertools
import re

from aoc_lib import Point2

with open("input.txt") as file:
    grid = [line.strip() for line in file.readlines()]

width = len(grid[0])
height = len(grid)

antennas: dict[str, list[Point2]] = {}
for match in re.finditer(r"[^.]", "".join(grid)):
    ant = match.group(0)
    if not ant in antennas:
        antennas[ant] = []
    antennas[ant].append(Point2(match.start() % width, int(match.start() / height)))

nodes: set[Point2] = set()
for ant, points in antennas.items():
    for (a, b) in itertools.combinations(points, 2):
        diff = b - a
        nodes.add(a)
        v = diff
        while True:
            p = a + v
            if p.x < 0 or width <= p.x or p.y < 0 or height <= p.y:
                break
            nodes.add(p)
            v = v + diff
        v = -diff
        while True:
            p = a + v
            if p.x < 0 or width <= p.x or p.y < 0 or height <= p.y:
                break
            nodes.add(p)
            v = v - diff
print(len(nodes))