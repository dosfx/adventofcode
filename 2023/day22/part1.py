from heapq import heapify, heappop
from typing import Dict, Set

class Brick:
    def __init__(self, id, x0: int, y0: int, z0: int, x1: int, y1: int, z1: int):
        self.id = id
        self.x0 = min(x0, x1)
        self.x1 = max(x0, x1)
        self.y0 = min(y0, y1)
        self.y1 = max(y0, y1)
        self.bot = min(z0, z1)
        self.top = max(z0, z1)
        self.x_dir = x0 != x1
        self.y_dir = y0 != y1
        self.z_dir = z0 != z1

    def down(self) -> None:
        self.top -= 1
        self.bot -= 1

    def above(self, other: "Brick") -> bool:
        if self.bot - 1 != other.top:
            return False
        if self.x0 != self.x1:
            if other.x1 < self.x0 or self.x1 < other.x0:
                return False
        elif self.x1 < other.x0 or other.x1 < self.x0:
            return False
        if self.y0 != self.y1:
            if other.y1 < self.y0 or self.y1 < other.y0:
                return False
        elif self.y1 < other.y0 or other.y1 < self.y0:
            return False
        return True

    def __lt__(self, other: "Brick") -> bool:
        return self.bot < other.bot

    def __repr__(self) -> str:
        return f"{self.id}:({self.x0},{self.x1})({self.y0},{self.y1})({self.bot},{self.top})"


    @staticmethod
    def parse(id: int, line: str) -> "Brick":
        coords = line.strip().split("~")
        return Brick(id, *([int(c) for c in coords[0].split(",")] + [int(c) for c in coords[1].split(",")]))

with open("input.txt") as file:
    bricks = [Brick.parse(id, line) for id,line in enumerate(file.readlines())]
heap = bricks.copy()
heapify(heap)

supporting: Dict[int, Set[int]] = {}
supported_by: Dict[int, Set[int]] = {}
done = False
while len(heap) > 0:
    brick = heap[0]
    if brick.bot == 1:
        heappop(heap)
        continue
    falling = True
    for other in bricks:
        if brick.above(other):
            falling = False
            if not brick.id in supported_by:
                supported_by[brick.id] = set()
            supported_by[brick.id].add(other.id)
            if not other.id in supporting:
                supporting[other.id] = set()
            supporting[other.id].add(brick.id)
    if falling:
        brick.down()
    else:
        heappop(heap)

total = 0
for brick in bricks:
    if not brick.id in supporting:
        total += 1
        continue
    for supported in supporting[brick.id]:
        if len(supported_by[supported]) == 1:
            break
    else:
        total += 1

print(total)