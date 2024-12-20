import itertools

from aoc_lib import StrGrid, Vector2

grid = StrGrid.from_file("input.txt")

antennas: dict[str, list[Vector2]] = {}
for x, y, ant in grid.findr(r"[^.]"):
    if not ant in antennas:
        antennas[ant] = []
    antennas[ant].append(Vector2(x, y))

nodes: set[Vector2] = set()
for ant, points in antennas.items():
    for (a, b) in itertools.combinations(points, 2):
        diff = b - a
        nodes.add(a)
        v = diff
        while True:
            p = a + v
            if not grid.containsp(p):
                break
            nodes.add(p)
            v = v + diff
        v = -diff
        while True:
            p = a + v
            if not grid.containsp(p):
                break
            nodes.add(p)
            v = v - diff
print(len(nodes))
