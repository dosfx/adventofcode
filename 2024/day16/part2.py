from dataclasses import dataclass, field
from queue import PriorityQueue
from aoc_lib import DIRECTIONS, StrGrid, Vector2, RIGHT


grid = StrGrid.from_file("input.txt")

start = [Vector2(x, y) for x, y, _ in grid.find("S")][0]
end = [Vector2(x, y) for x, y, _ in grid.find("E")][0]


@dataclass(order=True)
class QueueItem:
    cost: int
    p: Vector2 = field(compare=False)
    d: Vector2 = field(compare=False)
    path: set[Vector2] = field(compare=False)


best = 99999999
paths: set[Vector2] = set()
costs: dict[tuple[Vector2, Vector2], int] = {}
queue = PriorityQueue[QueueItem]()
for d in DIRECTIONS:
    queue.put(QueueItem(0, end, d, set([end])))
while not queue.empty():
    item = queue.get()
    if item.p == start:
        if item.d == RIGHT:
            if item.cost <= best:
                print(item.cost)
                best = item.cost
                paths = paths | item.path
                continue
    if grid.atp(item.p) == "#":
        continue
    if (item.p, item.d) in costs:
        if costs[(item.p, item.d)] < item.cost:
            continue
    costs[(item.p, item.d)] = item.cost
    queue.put(QueueItem(item.cost + 1, item.p + item.d,
              item.d, item.path | set([item.p])))
    queue.put(QueueItem(item.cost + 1000, item.p,
              item.d.clock, item.path | set([item.p])))
    queue.put(QueueItem(item.cost + 1000, item.p,
              item.d.counter, item.path | set([item.p])))

print(len(paths))
