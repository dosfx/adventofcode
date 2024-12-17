from dataclasses import dataclass, field
from queue import PriorityQueue
from aoc_lib import directions, StrGrid, Vector2, RIGHT


grid = StrGrid.from_file("input.txt")

start = [Vector2(x, y) for x, y, _ in grid.find("S")][0]
end = [Vector2(x, y) for x, y, _ in grid.find("E")][0]


@dataclass(order=True)
class QueueItem:
    cost: int
    p: Vector2 = field(compare=False)
    d: Vector2 = field(compare=False)


costs: dict[Vector2, int] = {}
queue = PriorityQueue[QueueItem]()
for d in directions:
    queue.put(QueueItem(0, end, d))
while not queue.empty():
    item = queue.get()
    if item.p == start:
        if item.d == RIGHT:
            print(item.cost)
        else:
            print(item.cost + 1000)
        break
    if grid.atp(item.p) == "#":
        continue
    if item.p in costs:
        if costs[item.p] < item.cost:
            continue
    costs[item.p] = item.cost
    queue.put(QueueItem(item.cost + 1, item.p + item.d, item.d))
    queue.put(QueueItem(item.cost + 1001, item.p + item.d.clock, item.d.clock))
    queue.put(QueueItem(item.cost + 1001, item.p +
              item.d.counter, item.d.counter))
