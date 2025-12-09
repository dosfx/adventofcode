from collections import deque
from aoc_lib import StrGrid, Vector2

grid = StrGrid.from_file("input.txt")
positions = [
    Vector2(x, y)
    for x in range(-1, 2)
    for y in range(-1, 2)
]
positions.remove(Vector2(0, 0))
count = 0
rolls = deque(grid.findp("@"))
qlen = 0
nlen = len(rolls)
while qlen != nlen:
    qlen = nlen
    for _ in range(qlen):
        p = rolls.popleft()
        if [grid.atp_none(p + v) for v in positions].count("@") < 4:
            grid.setp(p, ".")
            count += 1
        else:
            rolls.append(p)
    nlen = len(rolls)
print(count)
