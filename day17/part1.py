from heapq import heapify, heappop, heappush
from typing import List, Tuple

# cost, (x, y), dir, consec, path
Step = Tuple[int, Tuple[int, int], int, int, Tuple[Tuple[int, int]]]

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def move(x: int, y: int, dir: int) -> Tuple[int, int]:
    (dx, dy) = {
        NORTH: (0, -1),
        EAST: (1, 0),
        SOUTH: (0, 1),
        WEST: (-1, 0), 
    }[dir]
    return (x + dx, y + dy)


with open("input.txt") as file:
    grid = [[int(c) for c in line.strip()] for line in file.readlines()]
height = len(grid)
width = len(grid[0])

seen = set()
queue: List[Step] = [
    (0, (1, 0), EAST, 1, ()),
    (0, (0, 1), SOUTH, 1, ()),
]
heapify(queue)

count = 0
while len(queue) > 0:
    (cost, (x, y), dir, con, path) = heappop(queue)
    if x < 0 or width <= x or y < 0 or height <= y:
        continue
    if (x, y) in path:
        continue
    if con >= 3:
        continue
    path = path + ((x, y),)
    cost += grid[y][x]
    if x == width - 1 and y == height - 1:
        print(cost)
        break
    if (x, y, dir, con) in seen:
        continue
    seen.add((x, y, dir, con))
    heappush(queue, (cost, move(x, y, dir), dir, con + 1, path))
    left = (dir - 1) % 4
    heappush(queue, (cost, move(x, y, left), left, 0, path))
    right = (dir + 1) % 4
    heappush(queue, (cost, move(x, y, right), right, 0, path))
else:
    print("BAD")
