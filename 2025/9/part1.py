import itertools
from aoc_lib import Vector2, UNIT

with open("input.txt") as f:
    points = [Vector2(*[int(n) for n in line.split(",")])
              for line in f.readlines()]

max_area = 0
for a, b in itertools.combinations(points, 2):
    size = a - b + UNIT
    max_area = max(max_area, abs(size.x * size.y))
print(max_area)
