from collections import deque
from aoc_lib import DIRECTIONS, StrGrid, Vector2


SIZE = 71
with open("input.txt") as file:
    points = [Vector2(*map(int, file.readline().split(","))) for _ in range(1024)]


length = 0
END = Vector2(SIZE - 1, SIZE - 1)
visited = set[Vector2]()
queue = deque([Vector2(0, 0)])
while queue:
    for _ in range(len(queue)):
        cur = queue.popleft()
        if cur in visited:
            continue
        if cur == END:
            print(length)
            exit()
        visited.add(cur)
        for d in DIRECTIONS:
            nextp = cur + d
            if nextp.x < 0 or SIZE <= nextp.x or nextp.y < 0 or SIZE <= nextp.y:
                continue
            if nextp in points:
                continue
            queue.append(cur + d)
    length += 1
