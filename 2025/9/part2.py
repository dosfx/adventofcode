from heapq import heappop, heappush
import itertools
from aoc_lib import DIRECTIONS, Rectangle, StrGrid, Vector2


with open("input.txt") as f:
    points = [Vector2(*[int(n) for n in line.split(",")])
              for line in f.readlines()]

xmap = {}
for i, x in enumerate(sorted(set([p.x for p in points]))):
    xmap[x] = i
ymap = {}
for i, y in enumerate(sorted(set([p.y for p in points]))):
    ymap[y] = i


def comp(vec: Vector2) -> Vector2:
    return Vector2(xmap[vec.x], ymap[vec.y])


grid = StrGrid.from_size(len(xmap), len(ymap), ".")
lastc = comp(points[-1])
for p in points:
    c = comp(p)
    grid.setp(c, "#")
    diff = lastc - c
    direction = diff.norm()
    length = int(diff.len())
    for i in range(1, length):
        grid.setp(c + (direction * i), "#")
    lastc = c


def fill(p: Vector2) -> None:
    stack = [p]
    while len(stack) > 0:
        cur = stack.pop()
        if grid.atp_none(cur) != ".":
            continue
        grid.setp(cur, "#")
        for d in DIRECTIONS:
            stack.append(d + cur)


for x in range(grid.width):
    if grid.at(x, 0) == "#" and grid.at(x, 1) == ".":
        fill(Vector2(x, 1))
        break

with open("output.txt", "w") as f:
    f.writelines(str(grid))


class Node:
    def __init__(self, a: Vector2, b: Vector2):
        self.real = Rectangle.from_points(a, b)
        self.mapped = Rectangle.from_points(comp(a), comp(b))
        self.area = self.real.area

    def __lt__(self, other: "Node") -> bool:
        return self.area > other.area

    def contained(self) -> bool:
        for x in range(self.mapped.left, self.mapped.right):
            if grid.at(x, self.mapped.top) != "#":
                return False
            if grid.at(x, self.mapped.bot) != "#":
                return False
        for y in range(self.mapped.top, self.mapped.bot):
            if grid.at(self.mapped.left, y) != "#":
                return False
            if grid.at(self.mapped.right, y) != "#":
                return False
        return True


heap: list[Node] = []
for a, b in itertools.combinations(points, 2):
    heappush(heap, Node(a, b))

while len(heap) > 0:
    cur = heappop(heap)
    if cur.contained():
        break

print(cur.area, cur.real, cur.mapped)
