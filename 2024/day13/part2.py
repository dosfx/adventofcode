import re
from typing import cast

from aoc_lib import Vector2


def solve(p1: Vector2, p2: Vector2, prize: Vector2) -> int:
    # do some algebra
    # a.x1 + b.x2 = px  80.94 + 40.22   7520 + 880   8400
    # a.y1 + b.y2 = py  80.34 + 40.67   2720 + 2680  5400

    # a = (px - b.x2) / x1
    # a = (py - b.y2) / y1

    # y1(px - b.x2) = x1(py - b.y2)
    # y1.px - b.x2.y1 = x1.py - b.y2.x1
    # b.y2.x1 - b.x2.y1 = x1.py - y1.px
    # b(y2.x1 - x2.y1) = x1.py - y1.px
    # b = (x1.py - y1.px) / (y2.x1 - x2.y1)     (94.5400 - 34.8400) / (67.94 - 34.22)   (507600 - 285600) / (6298 - 748)     222000 / 5550

    b = ((p1.x * prize.y) - (p1.y * prize.x)) / ((p2.y * p1.x) - (p2.x * p1.y))
    a = (prize.x - (b * p2.x)) / p1.x
    if a == int(a) and b == int(b):
        return (3 * int(a)) + int(b)
    return 0


with open("input.txt") as file:
    total = 0
    while True:
        m = re.match(r"Button A: X\+(\d+), Y\+(\d+)", file.readline())
        if m is None:
            break
        but_a = Vector2(int(m.group(1)), int(m.group(2)))
        m = cast(re.Match[str], re.match(
            r"Button B: X\+(\d+), Y\+(\d+)", file.readline()))
        but_b = Vector2(int(m.group(1)), int(m.group(2)))
        m = cast(re.Match[str], re.match(
            r"Prize: X=(\d+), Y=(\d+)", file.readline()))
        prize = Vector2(int(m.group(1)) + 10000000000000, int(m.group(2)) + 10000000000000)
        file.readline()
        total += solve(but_a, but_b, prize)
print(total)
