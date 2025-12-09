from aoc_lib import StrGrid
from aoc_lib._vector2 import Vector2

grid = StrGrid.from_file("input.txt")
positions = [
    Vector2(x, y)
    for x in range(-1, 2)
    for y in range(-1, 2)
]
positions.remove(Vector2(0, 0))
count = 0
for p, c in grid.cellsp():
    if c != "@":
        continue
    if [grid.atp_none(p + v) for v in positions].count("@") < 4:
        count += 1
print(count)
