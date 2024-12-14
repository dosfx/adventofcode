import re
from typing import cast

from aoc_lib import Vector2

with open("input.txt") as file:
    robots: list[tuple[Vector2, Vector2]] = []
    for line in file.readlines():
        m = cast(re.Match[str], re.match(
            r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line))
        p = Vector2(int(m.group(1)), int(m.group(2)))
        v = Vector2(int(m.group(3)), int(m.group(4)))
        robots.append((p, v))

width = 101
height = 103


def visualize(positions: list[Vector2], w: int, h: int) -> None:
    counts: dict[Vector2, int] = {}
    for p in positions:
        counts[p] = counts.get(p, 0) + 1
    for y in range(h):
        for x in range(w):
            p = Vector2(x, y)
            if p in counts:
                print(str(counts[p]), end="")
            else:
                print(".", end="")
        print()

index = 0
while True:
    seconds = 11 + (101 * index)
    cur = [
        (p + (v * seconds)).mod2(width, height)
        for p, v in robots
    ]
    visualize(cur, width, height)
    input(seconds)
    seconds = 65 + (103 * index)
    cur = [
        (p + (v * seconds)).mod2(width, height)
        for p, v in robots
    ]
    visualize(cur, width, height)
    input(seconds)
    index += 1

# somthing seems to be happening around these 2 different patterns
# 11 112
# 65 168