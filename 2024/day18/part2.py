from collections import deque
from aoc_lib import DIRECTIONS, Vector2


SIZE = 71
START = Vector2(0, 0)
END = Vector2(SIZE - 1, SIZE - 1)
with open("input.txt") as file:
    points = [Vector2(*map(int, line.split(","))) for line in file.readlines()]

def solve(points: set[Vector2]) -> bool:
    visited = set[Vector2]()
    queue = deque([START])
    while queue:
        cur = queue.popleft()
        if cur in visited:
            continue
        if cur == END:
            return True
        visited.add(cur)
        for d in DIRECTIONS:
            nextp = cur + d
            if nextp.x < 0 or SIZE <= nextp.x or nextp.y < 0 or SIZE <= nextp.y:
                continue
            if nextp in points:
                continue
            queue.append(cur + d)
    return False

left = 0
right = len(points) - 1
while True:
    if right - left < 4:
        break
    mid = (left + right) // 2
    if solve(set(points[:mid])):
        left = mid
    else:
        right = mid

for i in range(left, right + 1):
    if not solve(set(points[:i])):
        p = points[i - 1]
        print(f"{p.x},{p.y}")
        break
